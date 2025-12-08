document.addEventListener('DOMContentLoaded', async ()=>{
  const s = await new Promise(resolve => chrome.storage.sync.get({githubToken:'', owner:'', repo:'', branch:'main'}, resolve));
  document.getElementById('token').value = s.githubToken || '';
  document.getElementById('owner').value = s.owner || '';
  document.getElementById('repo').value = s.repo || '';
  document.getElementById('branch').value = s.branch || 'main';

  document.getElementById('save').addEventListener('click', ()=>{
    const token = document.getElementById('token').value.trim();
    const owner = document.getElementById('owner').value.trim();
    const repo = document.getElementById('repo').value.trim();
    const branch = document.getElementById('branch').value.trim() || 'main';
    chrome.storage.sync.set({githubToken: token, owner, repo, branch}, ()=>{
      document.getElementById('status').textContent = 'Saved.';
    });
  });
});
