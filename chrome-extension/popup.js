// Popup script: extracts page HTML, prepares content, and opens a preview window for saving to GitHub.

async function querySettings() {
  return new Promise(resolve => chrome.storage.sync.get({
    githubToken: '',
    owner: '',
    repo: '',
    branch: 'main'
  }, resolve));
}

// Simple EPUB generator
function generateEPUB(title, html, savedDate) {
  function escapeXml(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
  }

  var epubContent = '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<html xmlns="http://www.w3.org/1999/xhtml">\n' +
    '<head><meta charset="UTF-8"/><title>' + escapeXml(title) + '</title>' + 
    '<meta name="saved_date" content="' + (savedDate || '') + '"/>' + 
    '<style>body{font-family:serif;margin:1em;line-height:1.5}</style></head>\n' + 
    '<body>\n<h1>' + escapeXml(title) + '</h1>\n' + html + '\n</body>\n</html>';
  
  return epubContent;
}

function toTitleCase(s){
  if(!s) return '';
  const cleaned = s.toString().replace(/[^A-Za-z0-9\s-]+/g,'').trim();
  return cleaned.split(/\s+/).map(w => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase()).join(' ');
}

function titleToFilename(s){
  const title = toTitleCase(s) || '';
  if(!title) return '';
  return title.replace(/\s+/g,' ');
}

// Basic HTML -> Markdown converter
function htmlToMarkdown(html, pageUrl){
  const doc = new DOMParser().parseFromString(html, 'text/html');

  function walk(node){
    if(node.nodeType === Node.TEXT_NODE){
      return node.nodeValue.replace(/\s+/g,' ');
    }
    if(node.nodeType !== Node.ELEMENT_NODE) return '';
    const tag = node.tagName.toLowerCase();
    if(tag.match(/^h[1-6]$/)){
      const level = parseInt(tag[1]);
      return '\n' + '#'.repeat(level) + ' ' + inner(node) + '\n\n';
    }
    if(tag === 'p'){
      return '\n' + inner(node) + '\n\n';
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
      let src = node.getAttribute('src') || 
                node.getAttribute('data-src') || 
                node.getAttribute('data-lazy-src') || 
                node.getAttribute('data-image') || '';
      if(src && pageUrl && !src.match(/^https?:\/\//)){
        try {
          src = new URL(src, pageUrl).href;
        } catch(e) {
          // If URL parsing fails, keep original src
        }
      }
      return src ? '![' + alt + '](' + src + ')' : '';
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
    return inner(node);
  }

  function inner(node){
    return Array.from(node.childNodes).map(walk).join('');
  }

  const article = doc.querySelector('article');
  if(article) return inner(article).trim();

  const main = doc.querySelector('main');
  if(main) return inner(main).trim();

  return inner(doc.body).trim();
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
      return {html: findArticle(), title: document.title, url: window.location.href};
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
    const messageInput = document.getElementById('message').value.trim() || 'Add article via extension';

    const page = await extractPage();
    const title = page.title || (new Date()).toISOString();
    const headingTitle = toTitleCase(title) || ((new Date()).toISOString());

    let contentText = '';
    let ext = 'md';
    const savedDate = new Date().toISOString();
    
    if(fmt === 'md'){
      const originalTitle = page.title || 'Untitled Article';
      const originalTitleQuoted = '"' + String(originalTitle).replace(/"/g,'\"') + '"';
      contentText = '---\nsaved_date: ' + savedDate + '\ntitle: ' + originalTitleQuoted + '\n---\n\n# ' + headingTitle + '\n\n' + htmlToMarkdown(page.html, page.url);
      ext = 'md';
    } else if(fmt === 'epub'){
      contentText = generateEPUB(title, htmlToMarkdown(page.html, page.url), savedDate);
      ext = 'epub';
    } else {
      contentText = '<!doctype html>\n<html><head><meta charset="utf-8"><title>' + title + '</title></head><body>' + page.html + '</body></html>';
      ext = 'html';
    }

    let filename = titleToFilename(page.title) || 'Article';
    filename = filename + '.' + ext;
    const path = 'Saved_Reading/' + filename;

    const existingSha = await getFileSha({owner:settings.owner, repo:settings.repo, path, branch: settings.branch, token: settings.githubToken});
    if(existingSha){
      statusEl.textContent = '⚠️ Article already saved! (' + filename + ')';
      return;
    }

    const pendingSaveData = {
      settings,
      path,
      contentText,
      messageInput
    };
    
    await chrome.storage.session.set({ pendingSaveData });
    
    chrome.tabs.create({ url: chrome.runtime.getURL('preview.html') });

    statusEl.textContent = 'Preview opened in a new tab.';
    setTimeout(() => window.close(), 1000);
    
  } catch(err){
    console.error(err);
    document.getElementById('status').textContent = 'Error: ' + err.message;
  }
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('saveBtn').addEventListener('click', onSave);

    document.getElementById('optionsLink').addEventListener('click', (e) => {
      e.preventDefault();
      chrome.runtime.openOptionsPage();
    });
});
