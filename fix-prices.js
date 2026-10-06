const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// Update size P
html = html.replace(/data-size="P" data-price="\d+"/g, 'data-size="P" data-price="25"');
html = html.replace(/(<span>Pequena<\/span><strong>R\$\s*)\d+(<\/strong>)/g, '$125$2');

// Update size M
html = html.replace(/data-size="M" data-price="\d+"/g, 'data-size="M" data-price="30"');
html = html.replace(/(<span>Média<\/span><strong>R\$\s*)\d+(<\/strong>)/g, '$130$2');

// Update size G
html = html.replace(/data-size="G" data-price="\d+"/g, 'data-size="G" data-price="35"');
html = html.replace(/(<span>Grande<\/span><strong>R\$\s*)\d+(<\/strong>)/g, '$135$2');

// Fix Marmita de Churrasco special prices
html = html.replace(/data-item="Marmita de Churrasco" data-size="M" data-price="\d+"/g, 'data-item="Marmita de Churrasco" data-size="M" data-price="34.99"');
html = html.replace(/(data-item="Marmita de Churrasco" data-size="M"[\s\S]*?<span>Média<\/span><strong>R\$\s*)\d+(<\/strong>)/g, '$134,99$2');

html = html.replace(/data-item="Marmita de Churrasco" data-size="G" data-price="\d+"/g, 'data-item="Marmita de Churrasco" data-size="G" data-price="39.99"');
html = html.replace(/(data-item="Marmita de Churrasco" data-size="G"[\s\S]*?<span>Grande<\/span><strong>R\$\s*)\d+(<\/strong>)/g, '$139,99$2');

fs.writeFileSync('index.html', html);
console.log('Prices updated successfully!');
