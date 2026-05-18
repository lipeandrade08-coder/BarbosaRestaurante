import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add new CSS for the cart icon and badge
cart_css = """
  .cart-btn { background: var(--blue-dk) !important; box-shadow: 0 6px 24px rgba(42,96,144,.35) !important; }
  .cart-btn:hover { background: var(--navy) !important; box-shadow: 0 10px 32px rgba(42,96,144,.5) !important; }
  .cart-icon-wrapper { position: relative; display: flex; align-items: center; justify-content: center; }
  .cart-icon { transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1); }
  .cart-badge {
    position: absolute; top: -8px; right: -10px;
    background: var(--gold); color: var(--navy);
    font-size: 0.65rem; font-weight: 800;
    width: 20px; height: 20px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    transform: scale(0); transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .cart-badge.has-items { transform: scale(1); }
  .cart-badge.pop { animation: badgePop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); }
  .cart-btn.bounce .cart-icon { animation: cartBounce 0.4s cubic-bezier(0.34, 1.56, 0.64, 1); }
  
  @keyframes badgePop { 0% { transform: scale(1); } 50% { transform: scale(1.4); } 100% { transform: scale(1); } }
  @keyframes cartBounce { 0% { transform: translateY(0); } 50% { transform: translateY(-4px); } 100% { transform: translateY(0); } }
</style>"""
content = content.replace("</style>", cart_css)

# 2. Replace the bar-send button HTML
old_button = """<button class="bar-send" onclick="openCart()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.123.558 4.116 1.534 5.843L0 24l6.335-1.54A11.943 11.943 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.003-1.368l-.36-.214-3.732.907.948-3.653-.236-.376A9.793 9.793 0 012.182 12C2.182 6.573 6.573 2.182 12 2.182S21.818 6.573 21.818 12 17.427 21.818 12 21.818z"/></svg>
      <span>Ver Resumo</span>
    </button>"""

new_button = """<button class="bar-send cart-btn" onclick="openCart()">
      <div class="cart-icon-wrapper">
        <svg class="cart-icon" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
          <circle cx="9" cy="21" r="1"></circle>
          <circle cx="20" cy="21" r="1"></circle>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
        </svg>
        <span id="cart-badge" class="cart-badge">0</span>
      </div>
      <span>Ver Resumo</span>
    </button>"""

content = content.replace(old_button, new_button)

# 3. Update the updateBar logic to handle the animation and count
old_update_bar = """  /* ── UPDATE BAR ── */
  function updateBar() {
    const bar = document.getElementById('order-bar');
    let total = order.price;
    let parts = [];
    if (order.item && order.size) parts.push(`${order.item} (${order.size})`);
    Object.entries(order.drinks).forEach(([k,v]) => {
      total += v.price * v.qty;
      parts.push(`${k} x${v.qty}`);
    });
    const hasItem = order.item && order.size;
    const hasDrink = Object.keys(order.drinks).length > 0;
    if (!hasItem && !hasDrink) { bar.classList.add('empty'); return; }
    bar.classList.remove('empty');
    document.getElementById('bar-items-text').textContent = parts.join(' · ') || '–';
    document.getElementById('bar-total-text').innerHTML = `<small>R$</small> ${total.toFixed(2).replace('.',',')}`;
  }"""

new_update_bar = """  /* ── UPDATE BAR ── */
  function updateBar() {
    const bar = document.getElementById('order-bar');
    let total = order.price;
    let parts = [];
    let itemCount = 0;
    
    if (order.item && order.size) { 
      parts.push(`${order.item} (${order.size})`);
      itemCount += 1;
    }
    
    Object.entries(order.drinks).forEach(([k,v]) => {
      total += v.price * v.qty;
      parts.push(`${k} x${v.qty}`);
      itemCount += v.qty;
    });
    
    const hasItem = order.item && order.size;
    const hasDrink = Object.keys(order.drinks).length > 0;
    
    const badge = document.getElementById('cart-badge');
    if (badge) {
        const oldQty = parseInt(badge.dataset.qty || 0);
        
        if (itemCount > 0) {
          badge.textContent = itemCount;
          badge.dataset.qty = itemCount;
          badge.classList.add('has-items');
          
          if (itemCount > oldQty) {
            badge.classList.remove('pop');
            document.querySelector('.cart-btn').classList.remove('bounce');
            void badge.offsetWidth; // trigger reflow
            badge.classList.add('pop');
            document.querySelector('.cart-btn').classList.add('bounce');
          }
        } else {
          badge.classList.remove('has-items');
          badge.dataset.qty = 0;
        }
    }

    if (!hasItem && !hasDrink) { bar.classList.add('empty'); return; }
    bar.classList.remove('empty');
    document.getElementById('bar-items-text').textContent = parts.join(' · ') || '–';
    document.getElementById('bar-total-text').innerHTML = `<small>R$</small> ${total.toFixed(2).replace('.',',')}`;
  }"""

content = content.replace(old_update_bar, new_update_bar)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Cart Icon and Animation!")
