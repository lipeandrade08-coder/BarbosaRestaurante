import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS adjustments for images
if '.drink-icon {' in content and 'background-size' not in content:
    content = content.replace('.drink-icon { font-size: 2.2rem; margin-bottom: 8px; }', 
                              '.drink-icon { width: 60px; height: 60px; margin: 0 auto 8px; border-radius: 50%; font-size: 2.2rem; display: flex; align-items: center; justify-content: center; }')

# Replace card emojis with background images
replacements = {
    'Marmita de Churrasco': ('<div class="card-img">🥩</div>', '<div class="card-img" style="background: url(\'img/marmita.png\') center/cover;"></div>'),
    'Kit Churrasco': ('<div class="card-img">🍖</div>', '<div class="card-img" style="background: url(\'img/kit.png\') center/cover;"></div>'),
    'Costela Desossada': ('<div class="card-img">🦴</div>', '<div class="card-img" style="background: url(\'img/costela.png\') center/cover;"></div>'),
    'Frango Grelhado': ('<div class="card-img">🍗</div>', '<div class="card-img" style="background: url(\'img/frango.png\') center/cover;"></div>'),
    'Frango à Milanesa': ('<div class="card-img">🍽️</div>', '<div class="card-img" style="background: url(\'https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?q=80&w=600&auto=format&fit=crop\') center/cover;"></div>'),
    'Filé de Peixe': ('<div class="card-img">🐟</div>', '<div class="card-img" style="background: url(\'https://images.unsplash.com/photo-1511317559916-56d5ddb625ce?q=80&w=600&auto=format&fit=crop\') center/cover;"></div>'),
    'Parmegiana de Frango': ('<div class="card-img">🧀</div>', '<div class="card-img" style="background: url(\'img/parmegiana.png\') center/cover;"></div>'),
    'Parmegiana de Carne': ('<div class="card-img">🥩</div>', '<div class="card-img" style="background: url(\'img/parmegiana.png\') center/cover;"></div>')
}

for title, (old_tag, new_tag) in replacements.items():
    # we need to find the specific one for the item
    # Since some use the same emoji, we can just replace within the context of the item
    pattern = r'(data-item="'+title+'"[^>]*>\s*)' + re.escape(old_tag)
    content = re.sub(pattern, r'\1' + new_tag.replace('\\', '\\\\'), content)

# Replace drinks
drink_replacements = {
    'Coca-Cola Lata': ('<div class="drink-icon">🥤</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Coca-Cola Zero Lata': ('<div class="drink-icon">🥤</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Schweppes Lata': ('<div class="drink-icon">🫧</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1513415564515-763d91423bdd?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Fanta Uva Lata': ('<div class="drink-icon">🍇</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1620863868661-042c1ef4cff3?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Fanta Laranja Lata': ('<div class="drink-icon">🍊</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1620863868661-042c1ef4cff3?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Guaraná Lata': ('<div class="drink-icon">🌿</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1581006852262-e4307cf6283a?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Suco Natural 1L': ('<div class="drink-icon">🍹</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1600271886742-f049cd451bba?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>'),
    'Coca-Cola 2L': ('<div class="drink-icon">🍾</div>', '<div class="drink-icon" style="background: url(\'https://images.unsplash.com/photo-1622483767028-3f66f32aef97?q=80&w=300&auto=format&fit=crop\') center/cover;"></div>')
}

for drink, (old_tag, new_tag) in drink_replacements.items():
    pattern = r'(data-drink="'+drink+'"[^>]*>\s*)' + re.escape(old_tag)
    content = re.sub(pattern, r'\1' + new_tag.replace('\\', '\\\\'), content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced successfully!")
