import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Scroll buttons
content = content.replace("onclick=\"scrollTo({top:document.getElementById('cardapio').offsetTop-80,behavior:'smooth'})\"", "onclick=\"scrollToSection('cardapio')\"")
content = content.replace("onclick=\"event.preventDefault();scrollTo({top:document.getElementById('cardapio').offsetTop-70,behavior:'smooth'})\"", "onclick=\"event.preventDefault();scrollToSection('cardapio')\"")
content = content.replace("onclick=\"event.preventDefault();scrollTo({top:document.getElementById('localizacao').offsetTop-70,behavior:'smooth'})\"", "onclick=\"event.preventDefault();scrollToSection('localizacao')\"")

# 2. Add Modal CSS
modal_css = """
  /* ── CART MODAL ── */
  .modal-overlay { position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(13,43,69,.6); backdrop-filter: blur(4px); z-index: 9999; display: flex; align-items: flex-end; justify-content: center; opacity: 0; pointer-events: none; transition: opacity .3s; }
  .modal-overlay.open { opacity: 1; pointer-events: auto; }
  .modal-content { background: var(--white); width: 100%; max-width: 500px; border-radius: 24px 24px 0 0; padding: 24px; transform: translateY(100%); transition: transform .3s cubic-bezier(.34,1.56,.64,1); max-height: 85vh; display: flex; flex-direction: column; }
  .modal-overlay.open .modal-content { transform: translateY(0); }
  .modal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
  .modal-header h2 { font-size: 1.5rem; color: var(--navy); font-family: 'Cormorant Garamond', serif; }
  .close-btn { background: none; border: none; font-size: 2rem; color: var(--gray); cursor: pointer; line-height: 1; }
  .modal-body { overflow-y: auto; flex: 1; padding-bottom: 20px; }
  .cart-item { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-bottom: 1px solid rgba(110,181,224,.2); }
  .cart-item-info { flex: 1; }
  .cart-item-title { font-weight: 600; color: var(--navy); font-size: .95rem; }
  .cart-item-desc { font-size: .8rem; color: var(--gray); }
  .cart-item-price { font-weight: 700; color: var(--blue-dk); margin-left: 12px; }
  .cart-item-actions { display: flex; align-items: center; gap: 10px; margin-left: 16px; }
  .remove-btn { color: #e74c3c; background: rgba(231,76,60,.1); border: none; padding: 6px 12px; border-radius: 50px; font-size: .75rem; font-weight: 600; cursor: pointer; }
  .cart-qty-ctrl { display: flex; align-items: center; gap: 8px; background: var(--off); border-radius: 50px; padding: 4px; }
  .cart-qty-ctrl button { width: 24px; height: 24px; border-radius: 50%; background: var(--blue); color: #fff; border: none; font-weight: bold; cursor: pointer; display: grid; place-items: center; }
  .cart-empty-msg { text-align: center; color: var(--gray); padding: 40px 0; }
"""
content = content.replace("</style>", modal_css + "</style>")

# 3. Add Modal HTML
modal_html = """
<!-- CART MODAL -->
<div id="cart-modal" class="modal-overlay" onclick="if(event.target==this) closeCart()">
  <div class="modal-content">
    <div class="modal-header">
      <h2>Resumo do Pedido</h2>
      <button class="close-btn" onclick="closeCart()">&times;</button>
    </div>
    <div class="modal-body" id="cart-items"></div>
    <div class="modal-footer" style="padding-top: 20px;">
      <button class="bar-send" style="width:100%; justify-content:center;" onclick="sendWhatsApp()">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.123.558 4.116 1.534 5.843L0 24l6.335-1.54A11.943 11.943 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.003-1.368l-.36-.214-3.732.907.948-3.653-.236-.376A9.793 9.793 0 012.182 12C2.182 6.573 6.573 2.182 12 2.182S21.818 6.573 21.818 12 17.427 21.818 12 21.818z"/></svg>
        <span>Enviar Pedido WhatsApp</span>
      </button>
    </div>
  </div>
</div>
<div id="toast"></div>
"""
content = content.replace('<div id="toast"></div>', modal_html)

# 4. Modify Sticky bar button
content = content.replace('<button class="bar-send" onclick="sendWhatsApp()">', '<button class="bar-send" onclick="openCart()">')
content = content.replace('<span>Enviar Pedido</span>', '<span>Ver Resumo</span>')

# 5. Add JS Functions
js_code = """
  function scrollToSection(id) {
    const el = document.getElementById(id);
    if(el) {
      const y = el.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({top: y, behavior: 'smooth'});
    }
  }

  function openCart() {
    renderCart();
    document.getElementById('cart-modal').classList.add('open');
  }

  function closeCart() {
    document.getElementById('cart-modal').classList.remove('open');
  }

  function renderCart() {
    const container = document.getElementById('cart-items');
    container.innerHTML = '';
    if (!order.item && Object.keys(order.drinks).length === 0) {
      container.innerHTML = '<div class="cart-empty-msg">Seu carrinho está vazio.</div>';
      return;
    }
    if (order.item) {
      container.innerHTML += `
        <div class="cart-item">
          <div class="cart-item-info">
            <div class="cart-item-title">${order.item}</div>
            <div class="cart-item-desc">Tamanho: ${order.size}</div>
          </div>
          <div class="cart-item-price">R$ ${order.price.toFixed(2).replace('.',',')}</div>
          <div class="cart-item-actions">
            <button class="remove-btn" onclick="removeMainItem()">Remover</button>
          </div>
        </div>
      `;
    }
    Object.entries(order.drinks).forEach(([name, data]) => {
      container.innerHTML += `
        <div class="cart-item">
          <div class="cart-item-info">
            <div class="cart-item-title">${name}</div>
            <div class="cart-item-desc">R$ ${data.price.toFixed(2).replace('.',',')} / un</div>
          </div>
          <div class="cart-item-price">R$ ${(data.price * data.qty).toFixed(2).replace('.',',')}</div>
          <div class="cart-item-actions">
            <div class="cart-qty-ctrl">
              <button onclick="updateCartDrink('${name}', -1)">−</button>
              <span style="font-weight:700;font-size:.85rem;min-width:16px;text-align:center">${data.qty}</span>
              <button onclick="updateCartDrink('${name}', 1)">+</button>
            </div>
          </div>
        </div>
      `;
    });
  }

  function removeMainItem() {
    order.item = null;
    order.size = null;
    order.price = 0;
    document.querySelectorAll('.menu-card').forEach(c => {
      c.classList.remove('selected');
      c.querySelectorAll('.price-pill').forEach(p => p.classList.remove('active'));
    });
    updateBar();
    renderCart();
    if (!order.item && Object.keys(order.drinks).length === 0) closeCart();
  }

  function updateCartDrink(name, delta) {
    if (!order.drinks[name]) return;
    order.drinks[name].qty += delta;
    if (order.drinks[name].qty < 1) {
      delete order.drinks[name];
      document.querySelectorAll('.drink-card').forEach(c => {
        if(c.dataset.drink === name) {
          c.classList.remove('selected');
          c.querySelector('.qty-num').textContent = '1';
        }
      });
    } else {
      document.querySelectorAll('.drink-card').forEach(c => {
        if(c.dataset.drink === name) {
          c.querySelector('.qty-num').textContent = order.drinks[name].qty;
        }
      });
    }
    updateBar();
    renderCart();
    if (!order.item && Object.keys(order.drinks).length === 0) closeCart();
  }
"""

content = content.replace("let order={item:null,size:null,price:0,drinks:{},tipo:'delivery',endereco:'',obs:''};", "let order={item:null,size:null,price:0,drinks:{},tipo:'delivery',endereco:'',obs:''};\n" + js_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Cart Updates")
