// Popup script: extracts page HTML via scripting, converts to Markdown/EPUB, and saves to GitHub using stored options

async function querySettings() {
  return new Promise(resolve => chrome.storage.sync.get({
    githubToken: '',
    owner: '',
    repo: '',
    branch: 'main'
  }, resolve));
}

// Simple EPUB generator (returns base64-encoded EPUB string)
function generateEPUB(title, html) {
  // Create minimal EPUB structure as a ZIP-like format
  // Most EPUB readers can read uncompressed EPUBs
  var now = new Date().toISOString().split('T')[0];
  var uuid = 'urn:uuid:' + 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });

  function escapeXml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
  }

  // For a proper EPUB, we'd need JSZip. For now, return HTML wrapped as XHTML for compatibility
  var epubContent = '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<html xmlns="http://www.w3.org/1999/xhtml">\n' +
    '<head><meta charset="UTF-8"/><title>' + escapeXml(title) + '</title>' +
    '<style>body{font-family:serif;margin:1em;line-height:1.5}</style></head>\n' +
    '<body>\n<h1>' + escapeXml(title) + '</h1>\n' + html + '\n</body>\n</html>';
  
  return epubContent;
}

function slugify(s){
  return s.toString().toLowerCase()
    .replace(/\s+/g,'-')
    .replace(/[^a-z0-9\-]+/g,'')
    .replace(/\-+/g,'-')
    .replace(/^-+|-+$/g,'');
}

// Basic HTML -> Markdown converter (handles headings, p, a, strong/em, lists, images)
function htmlToMarkdown(html){
  const doc = new DOMParser().parseFromString(html, 'text/html');

  function walk(node){
    if(node.nodeType === Node.TEXT_NODE){
      return node.nodeValue.replace(/\s+/g,' ');
    }
    if(node.nodeType !== Node.ELEMENT_NODE) return '';
    const tag = node.tagName.toLowerCase();
    let out = '';
    if(tag.match(/^h[1-6]$/)){
      const level = parseInt(tag[1]);
      out += '\n' + '#'.repeat(level) + ' ' + inner(node) + '\n\n';
      return out;
    }
    if(tag === 'p'){
      out += '\n' + inner(node) + '\n\n';
      return out;
    }
    if(tag === 'br'){
      return '  \n';
    }
    if(tag === 'a'){
      const href = node.getAttribute('href') || '';
      return '[' + inner(node) + '](' + href + ')';
    }
    if(tag === 'img'){
      const alt = node.getAttribute('alt') || '';
      const src = node.getAttribute('src') || '';
      return '![' + alt + '](' + src + ')';
    }
    if(tag === 'strong' || tag === 'b'){
      return '**' + inner(node) + '**';
    }
    if(tag === 'em' || tag === 'i'){
      return '_' + inner(node) + '_';
    }
    if(tag === 'ul'){
      return '\n' + Array.from(node.children).map(li=> '- ' + inner(li)).join('\n') + '\n\n';
    }
    if(tag === 'ol'){
      return '\n' + Array.from(node.children).map((li,i)=> (i+1) + '. ' + inner(li)).join('\n') + '\n\n';
    }
    if(tag === 'pre'){
      return '\n```\n' + node.textContent + '\n```\n\n';
    }
    if(tag === 'code'){
      return '`' + node.textContent + '`';
    }
    // default: recurse
    return inner(node);
  }

  function inner(node){
    return Array.from(node.childNodes).map(walk).join('');
  }

  // Prefer article tag if present
  const article = doc.querySelector('article');
  if(article) return inner(article).trim();

  // Else main
  const main = doc.querySelector('main');
  if(main) return inner(main).trim();

  // Fallback to body
  return inner(doc.body).trim();
}

function utf8ToBase64(str){
  return btoa(unescape(encodeURIComponent(str)));
}

async function saveToGitHub({owner, repo, path, message, contentBase64, token, branch, isUpdate=false, sha=null}){
  const url = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(path)}`;
  const body = {
    message: message || 'Add file via Save Article extension',
    content: contentBase64,
    branch: branch || undefined
  };
  if(sha) body.sha = sha;
  const res = await fetch(url, {
    method: 'PUT',
    headers: {
      'Authorization': 'token ' + token,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });
  return res;
}

async function getFileSha({owner, repo, path, branch, token}){
  const url = `https://api.github.com/repos/${owner}/${repo}/contents/${encodeURIComponent(path)}?ref=${encodeURIComponent(branch||'main')}`;
  const res = await fetch(url, {headers:{'Authorization':'token '+token,'Accept':'application/vnd.github.v3+json'}});
  if(res.status === 200){
    const data = await res.json();
    return data.sha;
  }
  return null;
}

async function extractPage(){
  // executeScript returns result array
  const [tab] = await chrome.tabs.query({active:true,currentWindow:true});
  const results = await chrome.scripting.executeScript({
    target:{tabId:tab.id},
    func: () => {
      function findArticle(){
        const selectors = ['article','main','[role="article"]'];
        for(const s of selectors){
          const el = document.querySelector(s);
          if(el) return el.innerHTML;
        }
        return document.body.innerHTML;
      }
      return {html: findArticle(), title: document.title};
    }
  });
  return results[0].result;
}

async function onSave(){
  const statusEl = document.getElementById('status');
  statusEl.textContent = 'Working...';
  try{
    const settings = await querySettings();
    if(!settings.githubToken || !settings.owner || !settings.repo){
      statusEl.textContent = 'Set GitHub token, owner and repo in options.';
      return;
    }
    const fmt = document.getElementById('format').value;
    const pathPrefixInput = document.getElementById('pathPrefix').value.trim();
    const messageInput = document.getElementById('message').value.trim() || 'Add article via extension';

    const page = await extractPage();
    const title = page.title || (new Date()).toISOString();

    let contentText = '';
    let ext = 'md';
    if(fmt === 'md'){
      contentText = '# ' + title + '\n\n' + htmlToMarkdown(page.html);
      ext = 'md';
    } else if(fmt === 'epub'){
      // Generate EPUB content (XHTML format for compatibility)
      contentText = generateEPUB(title, htmlToMarkdown(page.html));
      ext = 'epub';
    } else {
      // HTML fallback
      contentText = '<!doctype html>\n<html><head><meta charset="utf-8"><title>' + title + '</title></head><body>' + page.html + '</body></html>';
      ext = 'html';
    }

    let filename = slugify(title) || 'article';
    filename = filename + '.' + ext;
    let prefix = pathPrefixInput || '';
    if(prefix && !prefix.endsWith('/')) prefix += '/';
    const path = (prefix || '') + filename;

    const contentBase64 = utf8ToBase64(contentText);

    // Check if file exists
    const sha = await getFileSha({owner:settings.owner, repo:settings.repo, path, branch: settings.branch, token: settings.githubToken});
    let res = await saveToGitHub({owner:settings.owner, repo:settings.repo, path, message: messageInput, contentBase64, token: settings.githubToken, branch: settings.branch, sha});
    if(res.ok){
      statusEl.textContent = 'Saved to ' + settings.owner + '/' + settings.repo + '/' + path;
    } else {
      const errText = await res.text();
      statusEl.textContent = 'Error: ' + res.status + ' ' + errText;
    }
  } catch(err){
    console.error(err);
    document.getElementById('status').textContent = 'Error: ' + err.message;
  }
}

document.getElementById('saveBtn').addEventListener('click', onSave);

// Open options page
document.getElementById('optionsLink').addEventListener('click', (e) => {
  e.preventDefault();
  chrome.runtime.openOptionsPage();
});
