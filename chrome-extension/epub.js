// Minimal EPUB3 generator for browser (no external deps)
// Generates a simplified EPUB that can be read by most EPUB readers
(function(global){
  function EPUBGenerator(title, author, html) {
    this.title = title || 'Untitled';
    this.author = author || 'Unknown';
    this.html = html || '';
    this.uuid = this.generateUUID();
  }

  EPUBGenerator.prototype.generateUUID = function() {
    return 'urn:uuid:' + 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  };

  EPUBGenerator.prototype.escapeXml = function(str) {
    return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&apos;');
  };

  EPUBGenerator.prototype.generateEPUBFiles = function() {
    var now = new Date().toISOString().split('T')[0];
    var files = {};
    
    // mimetype (must be first, uncompressed, no newline)
    files['mimetype'] = 'application/epub+zip';
    
    // META-INF/container.xml
    files['META-INF/container.xml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n  <rootfiles>\n    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n  </rootfiles>\n</container>';
    
    // OEBPS/content.opf
    files['OEBPS/content.opf'] = '<?xml version="1.0" encoding="UTF-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid">\n  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n    <dc:title>' + this.escapeXml(this.title) + '</dc:title>\n    <dc:creator>' + this.escapeXml(this.author) + '</dc:creator>\n    <dc:identifier id="uid">' + this.uuid + '</dc:identifier>\n    <dc:date>' + now + '</dc:date>\n    <meta property="dcterms:modified">' + now + 'T00:00:00Z</meta>\n  </metadata>\n  <manifest>\n    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>\n    <item id="content" href="content.xhtml" media-type="application/xhtml+xml"/>\n  </manifest>\n  <spine>\n    <itemref idref="content" linear="yes"/>\n  </spine>\n</package>';
    
    // OEBPS/nav.xhtml
    files['OEBPS/nav.xhtml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n<head><title>Contents</title></head>\n<body>\n<nav epub:type="toc"><ol><li><a href="content.xhtml">' + this.escapeXml(this.title) + '</a></li></ol></nav>\n</body>\n</html>';
    
    // OEBPS/content.xhtml
    files['OEBPS/content.xhtml'] = '<?xml version="1.0" encoding="UTF-8"?>\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head><meta charset="UTF-8"/><title>' + this.escapeXml(this.title) + '</title><style>body{font-family:serif;margin:1em}</style></head>\n<body>\n<h1>' + this.escapeXml(this.title) + '</h1>\n' + this.html + '\n</body>\n</html>';
    
    return files;
  };

  EPUBGenerator.prototype.toBase64 = function() {
    // Build a simplified ZIP for EPUB (requires JSZip or manual ZIP construction)
    // For now, return base64-encoded JSON of files for manual ZIP construction
    var files = this.generateEPUBFiles();
    var json = JSON.stringify(files);
    return btoa(unescape(encodeURIComponent(json)));
  };

  global.EPUBGenerator = EPUBGenerator;
})(typeof window !== 'undefined' ? window : global);
