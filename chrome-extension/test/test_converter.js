// Test script: run with Node. Requires `jsdom`.
// Usage:
//   npm install jsdom
//   node chrome-extension/test/test_converter.js

const { JSDOM } = require('jsdom');

function slugify(s){
  return s.toString().toLowerCase()
    .replace(/\s+/g,'-')
    .replace(/[^a-z0-9\-]+/g,'')
    .replace(/\-+/g,'-')
    .replace(/^-+|-+$/g,'');
}

function htmlToMarkdownFromDocument(doc){
  function walk(node){
    if(node.nodeType === 3){ // TEXT_NODE
      return node.nodeValue.replace(/\s+/g,' ');
    }
    if(node.nodeType !== 1) return '';
    const tag = node.tagName.toLowerCase();
    if(tag.match(/^h[1-6]$/)){
      const level = parseInt(tag[1]);
      return '\n' + '#'.repeat(level) + ' ' + inner(node) + '\n\n';
    }
    if(tag === 'p') return '\n' + inner(node) + '\n\n';
    if(tag === 'br') return '  \n';
    if(tag === 'a'){
      const href = node.getAttribute('href') || '';
      return '[' + inner(node) + '](' + href + ')';
    }
    if(tag === 'img'){
      const alt = node.getAttribute('alt') || '';
      const src = node.getAttribute('src') || '';
      return '![' + alt + '](' + src + ')';
    }
    if(tag === 'strong' || tag === 'b') return '**' + inner(node) + '**';
    if(tag === 'em' || tag === 'i') return '_' + inner(node) + '_';
    if(tag === 'ul') return '\n' + Array.from(node.children).map(li=> '- ' + inner(li)).join('\n') + '\n\n';
    if(tag === 'ol') return '\n' + Array.from(node.children).map((li,i)=> (i+1) + '. ' + inner(li)).join('\n') + '\n\n';
    if(tag === 'pre') return '\n```\n' + node.textContent + '\n```\n\n';
    if(tag === 'code') return '`' + node.textContent + '`';
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

function utf8ToBase64(str){
  return Buffer.from(str, 'utf8').toString('base64');
}

async function run(){
  const sampleHtml = `
    <!doctype html>
    <html>
    <head><title>Test Article Title</title></head>
    <body>
      <article>
        <h1>Test Article Title</h1>
        <p>This is a <strong>sample</strong> paragraph with a <a href="https://example.com">link</a>.</p>
        <h2>Subheading</h2>
        <p>Another paragraph.</p>
        <ul><li>First item</li><li>Second item with <em>emphasis</em></li></ul>
        <pre><code>const x = 1;</code></pre>
        <img src="https://example.com/image.jpg" alt="An image">
      </article>
    </body>
    </html>
  `;

  const dom = new JSDOM(sampleHtml);
  const doc = dom.window.document;
  const title = doc.title || ('article-' + Date.now());
  const md = '# ' + title + '\n\n' + htmlToMarkdownFromDocument(doc);
  const filename = slugify(title) + '.md';
  const path = 'Saved_Reading/' + filename;
  const contentBase64 = utf8ToBase64(md);

  console.log('--- Markdown output ---');
  console.log(md);
  console.log('\n--- GitHub payload (simulated) ---');
  console.log(JSON.stringify({
    message: 'Add article via test',
    content: contentBase64,
    path
  }, null, 2));
}

run().catch(err=>{ console.error(err); process.exit(1); });
