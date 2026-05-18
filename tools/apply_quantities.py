import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

script_start = content.find("let order={item:null,size:null,price:0,drinks:{},tipo:'delivery',endereco:'',obs:''};")
script_end = content.find("  let toastTimer;")

new_script = """let order={items:{},drinks:{},tipo:'delivery',endereco:'',obs:''};

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
    const itemsKeys = Object.keys(order.items);
    const drinksKeys = Object.keys(order.drinks);
    
    if (itemsKeys.length === 0 && drinksKeys.length === 0) {
      container.innerHTML = '<div class="cart-empty-msg">Seu carrinho está vazio.</div>';
      return;
    }
    
    itemsKeys.forEach(k => {
      const data = order.items[k];
      container.innerHTML += `
        <div class="cart-item">
          <div class="cart-item-info">
            <div class="cart-item-title">${data.name}</div>
            <div class="cart-item-desc">Tamanho: ${data.size} – R$ ${data.price.toFixed(2).replace('.',',')} / un</div>
          </div>
          <div class="cart-item-price">R$ ${(data.price * data.qty).toFixed(2).replace('.',',')}</div>
          <div class="cart-item-actions">
            <div class="cart-qty-ctrl">
              <button onclick="updateCartItem('${k}', -1)">−</button>
              <span style="font-weight:700;font-size:.85rem;min-width:16px;text-align:center">${data.qty}</span>
              <button onclick="updateCartItem('${k}', 1)">+</button>
            </div>
          </div>
        </div>
      `;
    });
    
    drinksKeys.forEach(name => {
      const data = order.drinks[name];
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

  function updateCartItem(key, delta) {
    if (!order.items[key]) return;
    order.items[key].qty += delta;
    if (order.items[key].qty < 1) {
      delete order.items[key];
    }
    updateBar();
    renderCart();
    if (Object.keys(order.items).length === 0 && Object.keys(order.drinks).length === 0) closeCart();
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
    if (Object.keys(order.items).length === 0 && Object.keys(order.drinks).length === 0) closeCart();
  }

  function switchTab(id,btn){
    document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    document.getElementById('tab-'+id).classList.add('active');
    btn.classList.add('active');
  }

  function selectCard(card){
    // Highlight the card slightly, but don't deselect others because users can pick multiple items
    card.classList.add('selected');
    card.scrollIntoView({behavior:'smooth',block:'nearest'});
  }

  function selectSize(e,pill){
    e.stopPropagation();
    const card=pill.closest('.menu-card');
    const itemName = card.dataset.item;
    const size = pill.dataset.size;
    const price = parseInt(pill.dataset.price);
    const key = itemName + '|' + size;
    
    if(!order.items[key]){
      order.items[key] = { name: itemName, size: size, price: price, qty: 1 };
      showToast('✅ ' + itemName + ' (' + size + ') adicionado!');
    } else {
      order.items[key].qty++;
      showToast('✅ +1 ' + itemName + ' (' + size + ')');
    }
    
    card.classList.add('selected');
    pill.classList.add('active');
    // Remove active pill after a bit to show it's a clickable button rather than a radio state
    setTimeout(() => pill.classList.remove('active'), 200);
    
    updateBar();
  }

  function toggleDrink(card){
    if(event.target.closest('.qty-btn')) return;
    const name=card.dataset.drink;
    if(card.classList.contains('selected')){
      card.classList.remove('selected');
      delete order.drinks[name];
    } else {
      card.classList.add('selected');
      order.drinks[name]={qty:1,price:parseInt(card.dataset.price)};
    }
    updateBar();
  }

  function changeDrinkQty(e,btn,delta){
    e.stopPropagation();
    const card=btn.closest('.drink-card');
    const name=card.dataset.drink;
    const qspan=card.querySelector('.qty-num');
    let q=parseInt(qspan.textContent)+delta;
    if(q<1){toggleDrink(card);return;}
    qspan.textContent=q;
    if(order.drinks[name]) order.drinks[name].qty=q;
    updateBar();
  }

  function setTipo(t){
    order.tipo=t;
    ['delivery','retirada','local'].forEach(id=>document.getElementById('lbl-'+id).classList.remove('checked'));
    document.getElementById('lbl-'+t).classList.add('checked');
    document.getElementById('endereco-wrap').style.display=(t==='delivery')?'block':'none';
    updateBar();
  }

  document.getElementById('endereco').addEventListener('input',e=>{order.endereco=e.target.value;});
  document.getElementById('obs').addEventListener('input',e=>{order.obs=e.target.value;});

  function updateBar(){
    const bar=document.getElementById('order-bar');
    let total=0;
    let parts=[];
    let itemCount=0;
    
    Object.values(order.items).forEach(v => {
      total += v.price * v.qty;
      parts.push(v.name + ' (' + v.size + ') x' + v.qty);
      itemCount += v.qty;
    });
    
    Object.entries(order.drinks).forEach(([k,v])=>{
      total+=v.price*v.qty;
      parts.push(k+' x'+v.qty);
      itemCount+=v.qty;
    });
    
    const hasItems = Object.keys(order.items).length > 0;
    const hasDrink = Object.keys(order.drinks).length > 0;
    
    const badge = document.getElementById('cart-badge');
    if (badge) {
        const oldQty = parseInt(badge.dataset.qty || 0);
        if (itemCount > 0) {
          badge.textContent = itemCount;
          badge.dataset.qty = itemCount;
          badge.classList.add('has-items');
          if (itemCount > oldQty) {
            badge.style.animation = 'none';
            document.querySelector('.cart-btn .cart-icon').style.animation = 'none';
            void badge.offsetWidth;
            badge.style.animation = 'badgePop 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
            document.querySelector('.cart-btn .cart-icon').style.animation = 'cartBounce 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
          }
        } else {
          badge.classList.remove('has-items');
          badge.dataset.qty = 0;
        }
    }

    if(!hasItems&&!hasDrink){bar.classList.add('empty');return;}
    bar.classList.remove('empty');
    document.getElementById('bar-items-text').textContent=parts.join(' · ')||'–';
    document.getElementById('bar-total-text').innerHTML='<small>R$</small> '+total.toFixed(2).replace('.',',');
  }

  function sendWhatsApp(){
    if(Object.keys(order.items).length === 0 && Object.keys(order.drinks).length === 0){showToast('⚠️ Selecione pelo menos um prato!');return;}
    let total=0;
    let msg='🍖 *PEDIDO – Barbosa Restaurante*\n\n';
    
    if(Object.keys(order.items).length > 0){
      msg+='*Pratos:*\n';
      Object.values(order.items).forEach(v => {
        msg+='  • '+v.qty+'x '+v.name+' ('+v.size+') = R$'+(v.price*v.qty).toFixed(2).replace('.',',')+'\n';
        total+=v.price*v.qty;
      });
    }
    
    const dk=Object.entries(order.drinks);
    if(dk.length){
      msg+='\n*Bebidas:*\n';
      dk.forEach(([k,v])=>{
        msg+='  • '+v.qty+'x '+k+' = R$'+(v.price*v.qty).toFixed(2).replace('.',',')+'\n';
        total+=v.price*v.qty;
      });
    }
    msg+='\n*Subtotal (sem taxa):* R$'+total.toFixed(2).replace('.',',')+'\n';
    const tipoLabel={delivery:'🚴 Delivery',retirada:'🏃 Retirada',local:'🍽️ Comer no Estabelecimento'};
    msg+='*Tipo:* '+tipoLabel[order.tipo]+'\n';
    if(order.tipo==='delivery'&&order.endereco.trim()) msg+='*Endereço:* '+order.endereco.trim()+'\n';
    if(document.getElementById('obs').value.trim()) msg+='*Observações:* '+document.getElementById('obs').value.trim()+'\n';
    msg+='\n_A taxa de entrega será informada pelo restaurante._';
    window.open('https://wa.me/5512991136258?text='+encodeURIComponent(msg),'_blank');
  }

"""

if script_start != -1 and script_end != -1:
    content = content[:script_start] + new_script + content[script_end:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Quantities feature successfully applied!")
else:
    print("Could not find the script boundaries.")

