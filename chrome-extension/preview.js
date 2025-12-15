// --- Functions from popup.js

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

function markdownToHtml(md) {
  let html = md;

  // Remove YAML front matter
  html = html.replace(/^---[\s\S]*?---\n\n/, '');

  // Escape HTML special characters (but not in code blocks)
  const codeBlocks = [];
  html = html.replace(/```[\s\S]*?```/g, (match) => {
    codeBlocks.push(match);
    return `__CODE_BLOCK_${codeBlocks.length - 1}__`;
  });

  // Headings (must be before bold/italic)
  html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
  html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.*?)$/gm, '<h1>$1</h1>');
  html = html.replace(/^#### (.*?)$/gm, '<h4>$1</h4>');
  html = html.replace(/^##### (.*?)$/gm, '<h5>$1</h5>');
  html = html.replace(/^###### (.*?)$/gm, '<h6>$1</h6>');

  // Code blocks
  html = html.replace(/__CODE_BLOCK_(\d+)__/g, (match, idx) => {
    const block = codeBlocks[parseInt(idx)];
    const code = block.replace(/```/g, '').trim();
    return '<pre><code>' + escapeHtmlText(code) + '</code></pre>';
  });

  // Images (must be before links)
  html = html.replace(/!\[(.*?)\]\((.*?)\)/g, '<img src="$2" alt="$1" style="max-width:100%; height:auto; margin:10px 0;">');

  // Links
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');

  // Horizontal rules
  html = html.replace(/^\*{3,}$/gm, '<hr>');
  html = html.replace(/^-{3,}$/gm, '<hr>');
  html = html.replace(/^_{3,}$/gm, '<hr>');

  // Bold and italic (careful with order)
  html = html.replace(/\*\*\*(.*?)\*\*\*/g, '<strong><em>$1</em></strong>');
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/__(.*?)__/g, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
  html = html.replace(/_(.+?)_/g, '<em>$1</em>');

  // Inline code
  html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

  // Blockquotes
  html = html.replace(/^> (.*?)$/gm, '<blockquote>$1</blockquote>');

  // Lists
  html = html.replace(/^\* (.*?)$/gm, '<li>$1</li>');
  html = html.replace(/^- (.*?)$/gm, '<li>$1</li>');
  html = html.replace(/^\+ (.*?)$/gm, '<li>$1</li>');
  html = html.replace(/^\d+\. (.*?)$/gm, '<li>$1</li>');

  // Wrap consecutive <li> in <ul>
  html = html.replace(/(<li>.*?<\/li>(?:\n<li>.*?<\/li>)*)/g, '<ul>\n$1\n</ul>');

  // Paragraphs
  html = html.replace(/\n\n/g, '</p><p>');
  html = html.replace(/^(?!<[h|u|o|b|p|d|l])(.*?)$/gm, (match) => {
    if (match.trim() && !match.startsWith('<')) {
      return '<p>' + match + '</p>';
    }
    return match;
  });

  return html;
}

function escapeHtmlText(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}


// --- Main logic for preview page ---

document.addEventListener('DOMContentLoaded', () => {
  const contentDiv = document.getElementById('content');
  const statusEl = document.getElementById('status');
  const confirmSaveBtn = document.getElementById('confirmSaveBtn');
  const discardBtn = document.getElementById('discardBtn');

  let pendingSaveData = null;

  function showStatus(message, isError = false) {
    statusEl.textContent = message;
    statusEl.style.display = 'block';
    statusEl.style.color = isError ? '#dc3545' : '#28a745';
  }

  chrome.storage.session.get('pendingSaveData', (result) => {
    if (result.pendingSaveData && result.pendingSaveData.contentText) {
      pendingSaveData = result.pendingSaveData;
      const html = markdownToHtml(pendingSaveData.contentText);
      contentDiv.innerHTML = html;
      contentDiv.classList.remove('loading');
    } else {
      contentDiv.innerHTML = '<p style="color: #999;">No preview content available or data is corrupt. Please go back and try again.</p>';
      contentDiv.classList.remove('loading');
      confirmSaveBtn.disabled = true;
    }
  });

  confirmSaveBtn.addEventListener('click', async () => {
    if (!pendingSaveData) return;

    showStatus('Saving...');
    confirmSaveBtn.disabled = true;
    discardBtn.disabled = true;

    try {
      const contentBase64 = utf8ToBase64(pendingSaveData.contentText);
      const res = await saveToGitHub({
        owner: pendingSaveData.settings.owner,
        repo: pendingSaveData.settings.repo,
        path: pendingSaveData.path,
        message: pendingSaveData.messageInput,
        contentBase64: contentBase64,
        token: pendingSaveData.settings.githubToken,
        branch: pendingSaveData.settings.branch
      });

      if (res.ok) {
        showStatus('✓ Saved successfully to ' + pendingSaveData.path);
        // Clean up
        await chrome.storage.session.remove('pendingSaveData');
        setTimeout(() => window.close(), 2000);
      } else {
        const errData = await res.json();
        showStatus(`Error: ${errData.message || res.status}`, true);
        confirmSaveBtn.disabled = false;
        discardBtn.disabled = false;
      }
    } catch (err) {
      showStatus('Error: ' + err.message, true);
      confirmSaveBtn.disabled = false;
      discardBtn.disabled = false;
    }
  });

  discardBtn.addEventListener('click', async () => {
    await chrome.storage.session.remove('pendingSaveData');
    window.close();
  });
});