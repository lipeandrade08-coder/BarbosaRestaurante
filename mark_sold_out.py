import re

with open('/Users/mac/Documents/Barbosa Restaurante/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

available_items = [
    'Parmegiana de Frango',
    'Parmegiana de Carne',
    'Bife com Fritas',
    'Filé à Milanesa',
    'Panceta',
    'Churrasco',
    'Peixe'
]

# We need to find all menu-card divs.
# A regex to match a menu-card block until its card-name.
# Example:
# <div class="menu-card reveal">
#   <div class="card-img"...></div>
#   <div class="card-body">
#     <h3 class="card-name">Item Name</h3>

def replace_card(match):
    card_start = match.group(1)
    card_name = match.group(2)
    
    # Check if card_name is in available items
    is_available = any(available.lower() in card_name.lower() for available in available_items)
    
    # Add or remove sold-out
    if 'sold-out' in card_start:
        if is_available:
            card_start = card_start.replace(' sold-out', '')
    else:
        if not is_available:
            card_start = card_start.replace('menu-card reveal', 'menu-card reveal sold-out')
            
    return f"{card_start}{card_name}</h3>"

# Regex explanation:
# group 1: from <div class="menu-card reveal... up to <h3 class="card-name">
# group 2: the card name text
# This regex relies on the fact that <h3 class="card-name"> is shortly after the menu-card div
pattern = re.compile(r'(<div class="menu-card reveal[^>]*>.*?<h3 class="card-name">)(.*?)(</h3>)', re.DOTALL)

new_html = pattern.sub(replace_card, html)

with open('/Users/mac/Documents/Barbosa Restaurante/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Finished updating sold-out statuses.")
