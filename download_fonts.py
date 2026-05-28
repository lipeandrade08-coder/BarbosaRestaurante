import re
import os
import urllib.request

os.makedirs('css/fonts', exist_ok=True)

with open('css/fonts.css', 'r') as f:
    css_content = f.read()

# Find all url(...) patterns
urls = re.findall(r'url\((https://[^)]+\.(?:woff2|woff|ttf))\)', css_content)

for i, url in enumerate(urls):
    filename = f"font_{i}.woff2"
    filepath = os.path.join('css/fonts', filename)
    print(f"Downloading {url} to {filepath}")
    urllib.request.urlretrieve(url, filepath)
    
    # Replace the url in css
    css_content = css_content.replace(url, f"fonts/{filename}")

with open('css/fonts.css', 'w') as f:
    f.write(css_content)

print("Done")
