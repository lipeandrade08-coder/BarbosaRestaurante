import urllib.request
import re

drinks_to_download = {
    'Schweppes Lata': 'schweppes citrus lata 350ml frente branca',
    'Fanta Uva Lata': 'fanta uva lata 350ml frente branca',
    'Guaraná Lata': 'guarana antarctica lata 350ml frente branca',
    'Coca-Cola 2L': 'coca cola garrafa 2 litros pet frente branca'
}

filenames = {
    'Schweppes Lata': 'schweppes.jpg',
    'Fanta Uva Lata': 'fanta_uva.jpg',
    'Guaraná Lata': 'guarana.jpg',
    'Coca-Cola 2L': 'coca_2l.jpg'
}

for drink_name, query in drinks_to_download.items():
    q = urllib.parse.quote(query)
    url = f"https://tse2.mm.bing.net/th?q={q}&w=300&h=300&c=7&rs=1&p=0&dpr=1&pid=1.7"
    filepath = f"img/{filenames[drink_name]}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {drink_name} to {filepath}")
    except Exception as e:
        print(f"Error downloading {drink_name}: {e}")

# Update HTML to point to these new local images
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for drink_name, filename in filenames.items():
    pattern = r'(data-drink="'+re.escape(drink_name)+'"[^>]*>.*?background:\s*url\()[^\)]+(\))'
    content = re.sub(pattern, r'\g<1>img/'+filename+r'\g<2>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated with local downloaded drink images!")
