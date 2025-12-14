// Background service worker (currently unused but required by manifest)
// Set action icon on install/activate/runtime as a fallback in case Chrome
// didn't pick up the manifest's default_icon immediately.
self.addEventListener('install', ()=>{
  // noop
});
self.addEventListener('activate', ()=>{
  // noop
});

// Use runtime.onInstalled to set the icon explicitly (paths match manifest)
if (chrome && chrome.runtime && chrome.action && typeof chrome.action.setIcon === 'function') {
  chrome.runtime.onInstalled.addListener(() => {
    try {
      chrome.action.setIcon({path: {
        '16': 'icon16.png',
        '32': 'icon32.png',
        '48': 'icon48.png',
        '128': 'icon128.png'
      }}, () => {
        if (chrome.runtime.lastError) console.warn('setIcon warning:', chrome.runtime.lastError.message);
        else console.log('Action icon set from background.js');
      });
    } catch (e) {
      console.warn('setIcon failed:', e && e.message);
    }
  });
}
