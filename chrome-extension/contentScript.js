// This script returns the inner HTML of the article/main/body and the page title when executed via scripting.executeScript
(function(){
  function findArticle(){
    const selectors = ['article','main','[role="article"]'];
    for(const s of selectors){
      const el = document.querySelector(s);
      if(el) return el.innerHTML;
    }
    return document.body.innerHTML;
  }
  return { html: findArticle(), title: document.title };
})();
