import urllib.request, json, urllib.parse, re

queries = {
    'Coca-Cola Lata': 'coca cola lata 350ml',
    'Coca-Cola Zero Lata': 'coca cola sem açucar lata 350ml',
    'Schweppes Lata': 'schweppes citrus lata 350ml',
    'Fanta Uva Lata': 'fanta uva lata 350ml',
    'Fanta Laranja Lata': 'fanta laranja lata 350ml',
    'Guaraná Lata': 'guarana antarctica lata 350ml',
    'Suco Natural 1L': 'suco de laranja 900ml',
    'Coca-Cola 2L': 'coca cola garrafa 2 litros'
}

results = {}
for drink_name, q in queries.items():
    url = f"https://br.openfoodfacts.org/cgi/search.pl?search_terms={urllib.parse.quote(q)}&search_simple=1&action=process&json=1"
    try:
        req = urllib.request.urlopen(url)
        data = json.loads(req.read())
        for p in data.get('products', []):
            if p.get('image_front_url'):
                results[drink_name] = p['image_front_url']
                break
    except Exception as e:
        pass

print("Results from OFF:")
print(json.dumps(results, indent=2))

# Fallbacks if OFF didn't find anything
fallbacks = {
    'Coca-Cola Lata': 'https://images.openfoodfacts.org/images/products/789/490/001/1326/front_pt.3.400.jpg',
    'Coca-Cola Zero Lata': 'https://images.openfoodfacts.org/images/products/789/490/001/0145/front_pt.10.400.jpg',
    'Schweppes Lata': 'https://images.openfoodfacts.org/images/products/789/490/053/0005/front_pt.28.400.jpg',
    'Fanta Uva Lata': 'https://images.openfoodfacts.org/images/products/789/490/070/0040/front_pt.45.400.jpg',
    'Fanta Laranja Lata': 'https://images.openfoodfacts.org/images/products/789/490/001/1562/front_pt.10.400.jpg',
    'Guaraná Lata': 'https://images.openfoodfacts.org/images/products/789/199/100/1063/front_pt.30.400.jpg',
    'Suco Natural 1L': 'https://images.openfoodfacts.org/images/products/789/824/316/0136/front_pt.11.400.jpg',
    'Coca-Cola 2L': 'https://images.openfoodfacts.org/images/products/789/490/001/1517/front_pt.72.400.jpg'
}

for k, v in fallbacks.items():
    if k not in results:
        results[k] = v

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for drink, img_url in results.items():
    # Replace existing background url in style="..." for that drink
    pattern = r'(data-drink="'+re.escape(drink)+'"[^>]*>.*?background:\s*url\()[^\)]+(\))'
    content = re.sub(pattern, r'\g<1>'+img_url+r'\g<2>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated!")
