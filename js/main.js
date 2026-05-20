// CONFIGURAÇÃO
const WHATSAPP_NUMBER = "5512991136258";

let cart = { items: {}, drinks: {} };
let currentStep = 1;
let orderType = 'Entrega';
let paymentMethod = 'Dinheiro';

// Sanitizador de HTML — previne XSS ao injetar dados do usuário via innerHTML
function esc(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function setOrderType(type, btn) {
  orderType = type;
  document.querySelectorAll('#step-2 .tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('delivery-fields').style.display = type === 'Entrega' ? 'block' : 'none';
}

function setPayment(method, btn) {
  paymentMethod = method;
  document.querySelectorAll('.pay-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  const hint = document.getElementById('pix-hint');
  method === 'PIX' ? hint.classList.add('visible') : hint.classList.remove('visible');
}

function clearCart() {
  if (confirm('Deseja realmente limpar todo o seu pedido?')) {
    cart = { items: {}, drinks: {} };
    document.querySelectorAll('.drink-card').forEach(c => c.classList.remove('selected'));
    document.querySelectorAll('.price-pill').forEach(p => {
      p.classList.remove('has-items');
      const v = p.querySelector('.pill-qty-val');
      if (v) v.textContent = '0';
    });
    updateUI();
    closeModal();
    showToast('🗑️ Carrinho esvaziado!');
  }
}

function resetCartSilent() {
  cart = { items: {}, drinks: {} };
  document.querySelectorAll('.drink-card').forEach(c => c.classList.remove('selected'));
  document.querySelectorAll('.price-pill').forEach(p => {
    p.classList.remove('has-items');
    const v = p.querySelector('.pill-qty-val');
    if (v) v.textContent = '0';
  });
  updateUI();
  closeModal();

  // Reset do formulário para evitar que dados de um cliente vazem para o próximo
  const elName = document.getElementById('order-name');
  if (elName) elName.value = '';
  
  const elObs = document.getElementById('order-obs');
  if (elObs) elObs.value = '';
  
  const elCep = document.getElementById('order-cep');
  if (elCep) elCep.value = '';
  
  resetCEPFields();

  const btnDelivery = document.getElementById('type-delivery');
  if (btnDelivery) setOrderType('Entrega', btnDelivery);

  const btnPay = document.querySelector('.pay-btn'); // O primeiro é Dinheiro
  if (btnPay) setPayment('Dinheiro', btnPay);
}

function switchTab(id, btn) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  // Restringe ao elemento pai do botão clicado (a div .menu-tabs)
  btn.closest('.menu-tabs').querySelectorAll('.tab-btn')
    .forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  btn.classList.add('active');
}

function handlePillClick(pill) {
  const key = `${pill.dataset.item}|${pill.dataset.size}`;
  if (pill.classList.contains('has-items')) return;
  cart.items[key] = cart.items[key]
    ? { ...cart.items[key], qty: cart.items[key].qty + 1 }
    : { name: pill.dataset.item, size: pill.dataset.size, price: parseInt(pill.dataset.price), qty: 1 };
  syncPill(pill, key);
  showToast(`✅ ${pill.dataset.item} (${pill.dataset.size}) adicionado!`);
  updateUI();
}

function pillQtyChange(btn, delta, e) {
  e.stopPropagation();
  const pill = btn.closest('.price-pill');
  const key = `${pill.dataset.item}|${pill.dataset.size}`;
  if (!cart.items[key]) return;
  cart.items[key].qty += delta;
  if (cart.items[key].qty < 1) delete cart.items[key];
  syncPill(pill, key);
  updateUI();
}

function syncPill(pill, key) {
  const qty = cart.items[key] ? cart.items[key].qty : 0;
  const v = pill.querySelector('.pill-qty-val');
  if (v) v.textContent = qty;
  pill.classList.toggle('has-items', qty > 0);
}

function toggleDrink(name, price, card) {
  if (cart.drinks[name]) {
    delete cart.drinks[name];
    card.classList.remove('selected');
  } else {
    cart.drinks[name] = { price, qty: 1 };
    card.classList.add('selected');
  }
  updateUI();
}

function updateDrinkQty(name, delta, e) {
  e.stopPropagation();
  if (!cart.drinks[name]) return;
  cart.drinks[name].qty += delta;
  if (cart.drinks[name].qty < 1) {
    delete cart.drinks[name];
    // Null-check + CSS.escape para nomes com caracteres especiais
    const card = document.querySelector(`.drink-card[data-drink="${CSS.escape(name)}"]`);
    if (card) card.classList.remove('selected');
  }
  updateUI();
}

function updateUI() {
  let total = 0;
  let count = 0;

  Object.values(cart.items).forEach(i => {
    total += i.price * i.qty;
    count += i.qty;
  });

  Object.entries(cart.drinks).forEach(([name, data]) => {
    total += data.price * data.qty;
    count += data.qty;
    const card = document.querySelector(`.drink-card[data-drink="${CSS.escape(name)}"]`);
    if (card) card.querySelector('.qty-val').innerText = data.qty;
  });

  const bar = document.getElementById('order-bar');
  if (count > 0) {
    bar.classList.remove('hidden');
    document.getElementById('bar-total').innerHTML = `<small>R$</small> ${total.toFixed(2).replace('.', ',')}`;
    document.getElementById('bar-items').innerText = `${count} ${count === 1 ? 'item selecionado' : 'itens selecionados'}`;
    document.getElementById('cart-count').innerText = count;
  } else {
    bar.classList.add('hidden');
  }
}

function openModal() {
  document.body.style.overflow = 'hidden'; // Trava o scroll do body (fix iOS Safari)
  renderCartList();
  document.getElementById('modal-checkout').classList.add('active');
  goToStep(1);
  // Reseta campos de CEP a cada abertura do modal
  document.getElementById('order-cep').value = '';
  resetCEPFields();
}

function closeModal() {
  document.body.style.overflow = ''; // Restaura o scroll ao fechar
  document.getElementById('modal-checkout').classList.remove('active');
}

function renderCartList() {
  const list = document.getElementById('cart-items-list');
  list.innerHTML = '';
  let total = 0;

  Object.entries(cart.items).forEach(([key, item]) => {
    total += item.price * item.qty;
    // Usa esc() em todos os dados do usuário para prevenir XSS via innerHTML
    const safeName = esc(item.name);
    const safeSize = esc(item.size);
    const row = document.createElement('div');
    row.className = 'cart-item-row';
    row.innerHTML = `
      <div class="item-info">
        <h4>${safeName}</h4>
        <p>Tamanho: ${safeSize} • R$ ${item.price.toFixed(2).replace('.', ',')} un</p>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <strong style="color: var(--blue-dk)">R$ ${(item.price * item.qty).toFixed(2).replace('.', ',')}</strong>
        <div class="drink-qty" style="display: flex">
          <span style="font-weight: 700; min-width: 20px; text-align: center">${item.qty}</span>
        </div>
      </div>
    `;
    // Botões criados via JS para evitar injeção de código no atributo onclick
    const btnMinus = document.createElement('button');
    btnMinus.className = 'qty-btn';
    btnMinus.textContent = '−';
    btnMinus.onclick = () => updateItemQty(key, -1);
    const btnPlus = document.createElement('button');
    btnPlus.className = 'qty-btn';
    btnPlus.textContent = '+';
    btnPlus.onclick = () => updateItemQty(key, 1);
    const qtyDiv = row.querySelector('.drink-qty');
    qtyDiv.insertBefore(btnMinus, qtyDiv.firstChild);
    qtyDiv.appendChild(btnPlus);
    list.appendChild(row);
  });

  Object.entries(cart.drinks).forEach(([name, data]) => {
    total += data.price * data.qty;
    const safeDrinkName = esc(name);
    const row = document.createElement('div');
    row.className = 'cart-item-row';
    row.innerHTML = `
      <div class="item-info">
        <h4>${safeDrinkName}</h4>
        <p>R$ ${data.price.toFixed(2).replace('.', ',')} un</p>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <strong style="color: var(--blue-dk)">R$ ${(data.price * data.qty).toFixed(2).replace('.', ',')}</strong>
        <div class="drink-qty" style="display: flex">
          <span style="font-weight: 700; min-width: 20px; text-align: center">${data.qty}</span>
        </div>
      </div>
    `;
    const btnMinus = document.createElement('button');
    btnMinus.className = 'qty-btn';
    btnMinus.textContent = '−';
    btnMinus.onclick = () => updateDrinkQtyModal(name, -1);
    const btnPlus = document.createElement('button');
    btnPlus.className = 'qty-btn';
    btnPlus.textContent = '+';
    btnPlus.onclick = () => updateDrinkQtyModal(name, 1);
    const qtyDiv = row.querySelector('.drink-qty');
    qtyDiv.insertBefore(btnMinus, qtyDiv.firstChild);
    qtyDiv.appendChild(btnPlus);
    list.appendChild(row);
  });

  document.getElementById('modal-total-val').innerText = `R$ ${total.toFixed(2).replace('.', ',')}`;
}

function updateItemQty(key, delta) {
  if (!cart.items[key]) return; // Guard: evita TypeError em cliques rápidos
  cart.items[key].qty += delta;
  if (cart.items[key].qty < 1) delete cart.items[key];
  const [iName, iSize] = key.split('|');
  document.querySelectorAll('.price-pill').forEach(p => {
    if (p.dataset.item === iName && p.dataset.size === iSize) syncPill(p, key);
  });
  renderCartList();
  updateUI();
  if (Object.keys(cart.items).length === 0 && Object.keys(cart.drinks).length === 0) closeModal();
}

function updateDrinkQtyModal(name, delta) {
  if (!cart.drinks[name]) return; // Guard: evita TypeError em cliques rápidos
  cart.drinks[name].qty += delta;
  if (cart.drinks[name].qty < 1) {
    delete cart.drinks[name];
    // Null-check: evita crash caso o card não esteja no DOM
    const card = document.querySelector(`.drink-card[data-drink="${CSS.escape(name)}"]`);
    if (card) card.classList.remove('selected');
  }
  renderCartList();
  updateUI();
  if (Object.keys(cart.items).length === 0 && Object.keys(cart.drinks).length === 0) closeModal();
}

function goToStep(s) {
  currentStep = s;
  document.querySelectorAll('.step-content').forEach(c => c.classList.remove('active'));
  document.getElementById('step-' + s).classList.add('active');

  const titleEl = document.getElementById('modal-title');
  if (titleEl) {
    if (s === 1) titleEl.innerText = "Seu Pedido";
    else if (s === 2) titleEl.innerText = "Seus Dados";
    else if (s === 3) titleEl.innerText = "Confirmar Pedido";
  }

  document.querySelectorAll('.step-dot').forEach((d, i) => {
    d.classList.toggle('active', i < s);
  });

  document.getElementById('btn-back').style.display = s > 1 ? 'block' : 'none';
  document.getElementById('btn-next').style.display = s < 3 ? 'block' : 'none';
  document.getElementById('btn-finish').style.display = s === 3 ? 'flex' : 'none';

  if (s === 3) renderSummary();
}

function nextStep() {
  if (currentStep === 1) {
    const totalItems = Object.keys(cart.items).length + Object.keys(cart.drinks).length;
    if (totalItems === 0) { showToast('⚠️ Adicione pelo menos um item ao pedido.'); return; }
  }
  if (currentStep === 2) {
    const name = document.getElementById('order-name').value.trim();
    if (!name) { showToast('⚠️ Por favor, informe seu nome.'); return; }

    if (orderType === 'Entrega') {
      const cep = document.getElementById('order-cep').value.replace(/\D/g, '');
      const numero = document.getElementById('order-numero').value.trim();
      const ref = document.getElementById('order-reference').value.trim();
      const rua = document.getElementById('order-rua').value.trim();
      if (cep.length !== 8 || !rua) { showToast('⚠️ Informe um CEP válido para buscar o endereço.'); return; }
      if (!numero) { showToast('⚠️ Informe o número da residência.'); return; }
      if (!ref) { showToast('⚠️ Informe um ponto de referência.'); return; }
    }
  }
  goToStep(currentStep + 1);
}

function prevStep() { goToStep(currentStep - 1); }

function addMoreItems() {
  closeModal();
  setTimeout(() => {
    const cardapio = document.getElementById('cardapio');
    window.scrollTo({ top: cardapio.offsetTop - 80, behavior: 'smooth' });
    showToast('🛒 Carrinho mantido! Adicione mais itens e clique em "Ver Pedido".');
  }, 300); // Aguarda o modal fechar antes de rolar
}

function renderSummary() {
  const summary = document.getElementById('order-summary');
  const name = document.getElementById('order-name').value;
  const rua = document.getElementById('order-rua').value;
  const bairro = document.getElementById('order-bairro').value;
  const cidade = document.getElementById('order-cidade').value;
  const numero = document.getElementById('order-numero').value;
  const cep = document.getElementById('order-cep').value;
  const ref = document.getElementById('order-reference').value;
  const obs = document.getElementById('order-obs').value;
  const fullAddr = rua ? `${rua}, ${numero} — ${bairro}, ${cidade} (CEP ${cep})` : '';

  // esc() sanitiza dados do usuário para prevenir XSS via innerHTML
  let html = `<p style="margin-bottom: 8px;"><strong>Cliente:</strong> ${esc(name)}</p>`;
  html += `<p style="margin-bottom: 8px;"><strong>Tipo:</strong> ${orderType}</p>`;
  html += `<p style="margin-bottom: 8px;"><strong>Pagamento:</strong> ${paymentMethod}</p>`;

  if (orderType === 'Entrega') {
    html += `<p style="margin-bottom: 8px;"><strong>Endereço:</strong> ${esc(fullAddr)}</p>`;
    html += `<p style="margin-bottom: 8px;"><strong>Referência:</strong> ${esc(ref)}</p>`;
  }

  if (obs) html += `<p style="margin-bottom: 8px;"><strong>Obs:</strong> ${esc(obs)}</p>`;

  html += `<div style="border-top: 1px solid rgba(0,0,0,0.05); padding-top: 12px; margin-top: 12px;">`;
  Object.values(cart.items).forEach(i => {
    html += `<p style="font-size: 0.9rem; margin-bottom: 4px;">${i.qty}x ${esc(i.name)} (${esc(i.size)})</p>`;
  });
  Object.entries(cart.drinks).forEach(([name, data]) => {
    html += `<p style="font-size: 0.9rem; margin-bottom: 4px;">${data.qty}x ${esc(name)}</p>`;
  });
  html += `</div>`;

  summary.innerHTML = html;
}

function finishOrder() {
  const btnFinish = document.getElementById('btn-finish');
  if (btnFinish) {
    if (btnFinish.disabled) return;
    btnFinish.disabled = true;
    setTimeout(() => { btnFinish.disabled = false; }, 2000);
  }

  const name = document.getElementById('order-name').value;
  const rua = document.getElementById('order-rua').value;
  const bairro = document.getElementById('order-bairro').value;
  const cidade = document.getElementById('order-cidade').value;
  const numero = document.getElementById('order-numero').value;
  const cep = document.getElementById('order-cep').value;
  const ref = document.getElementById('order-reference').value;
  const obs = document.getElementById('order-obs').value;
  const fullAddr = rua ? `${rua}, ${numero} — ${bairro}, ${cidade} (CEP ${cep})` : '';

  let itemsList = '';
  let total = 0;
  Object.values(cart.items).forEach(i => {
    itemsList += `• ${i.qty}x ${i.name} (${i.size}) - R$ ${(i.price * i.qty).toFixed(2).replace('.', ',')}\n`;
    total += i.price * i.qty;
  });

  Object.entries(cart.drinks).forEach(([drinkName, data]) => {
    itemsList += `• ${data.qty}x ${drinkName} - R$ ${(data.price * data.qty).toFixed(2).replace('.', ',')}\n`;
    total += data.price * data.qty;
  });

  // 1. Abre o WhatsApp
  let msg = `*PEDIDO - Barbosa Restaurante*\n\n`;
  msg += `*Cliente:* ${name}\n`;
  msg += `*Tipo:* ${orderType}\n`;
  msg += `*Pagamento:* ${paymentMethod}\n`;

  if (orderType === 'Entrega') {
    msg += `*Endereço:* ${fullAddr}\n`;
    msg += `*Referência:* ${ref}\n`;
  }

  msg += `\n*Itens:*\n${itemsList}`;
  msg += `\n*Subtotal:* R$ ${total.toFixed(2).replace('.', ',')}\n`;
  if (obs) msg += `\n*Observações:* ${obs}\n`;

  msg += `\n_Favor informar a taxa de entrega e tempo estimado._`;

  showToast('✅ Pedido enviado! Abrindo WhatsApp...');

  window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener,noreferrer');
  // 4. Limpa o carrinho silenciosamente e fecha o modal
  resetCartSilent();
}

function showToast(msg) {
  const t = document.getElementById('toast');
  t.innerText = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 3000);
}

function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) window.scrollTo({ top: el.offsetTop - 80, behavior: 'smooth' });
}

/* ===== CEP AUTO-FILL (ViaCEP) ===== */
let _cepController = null; // AbortController da última requisição CEP

function formatCEP(input) {
  let v = input.value.replace(/\D/g, '').slice(0, 8);
  if (v.length > 5) v = v.slice(0, 5) + '-' + v.slice(5);
  input.value = v;
  const digits = v.replace(/\D/g, '');
  if (digits.length === 8) fetchCEP(digits);
  else resetCEPFields();
}

async function fetchCEP(cep) {
  // Cancela requisição anterior se o usuário digitou outro CEP
  if (_cepController) _cepController.abort();
  _cepController = new AbortController();
  const signal = _cepController.signal;

  const spinner = document.getElementById('cep-spinner');
  const okIcon = document.getElementById('cep-ok');
  const errIcon = document.getElementById('cep-error');
  const msg = document.getElementById('cep-msg');

  spinner.style.display = 'block';
  okIcon.style.display = 'none';
  errIcon.style.display = 'none';
  msg.style.display = 'none';
  resetCEPFields();

  try {
    const res = await fetch(`https://viacep.com.br/ws/${cep}/json/`, { signal });
    const data = await res.json();
    spinner.style.display = 'none';

    if (data.erro) {
      errIcon.style.display = 'block';
      msg.textContent = 'CEP não encontrado. Verifique e tente novamente.';
      msg.style.color = '#e74c3c';
      msg.style.display = 'block';
      return;
    }

    // Preenche os campos automaticamente
    document.getElementById('order-rua').value = data.logradouro || '';
    document.getElementById('order-bairro').value = data.bairro || '';
    document.getElementById('order-cidade').value = `${data.localidade} / ${data.uf}`;

    // Mostra os campos de endereço
    document.getElementById('addr-rua-group').style.display = 'block';
    document.getElementById('addr-bairro-cidade-group').style.display = 'grid';
    document.getElementById('addr-numero-group').style.display = 'block';
    document.getElementById('addr-ref-group').style.display = 'block';

    okIcon.style.display = 'block';
    msg.textContent = `📍 ${data.logradouro ? data.logradouro + ', ' : ''}${data.bairro}, ${data.localidade} – ${data.uf}`;
    msg.style.color = 'var(--gray)';
    msg.style.display = 'block';

    // Foca no campo número
    setTimeout(() => document.getElementById('order-numero').focus(), 100);

  } catch (e) {
    // Ignora silenciosamente se foi cancelamento intencional (AbortError)
    if (e.name === 'AbortError') return;

    spinner.style.display = 'none';

    // ── Fallback manual: ViaCEP indisponível ────────────────────────────
    errIcon.style.display = 'block';
    msg.innerHTML = '⚠️ Não foi possível buscar o CEP automaticamente. <strong>Preencha o endereço manualmente abaixo.</strong>';
    msg.style.color = '#e67e22';
    msg.style.display = 'block';

    // Torna os campos de rua/bairro/cidade editáveis para preenchimento manual
    ['order-rua', 'order-bairro', 'order-cidade'].forEach(id => {
      const el = document.getElementById(id);
      if (!el) return;
      el.removeAttribute('readonly');
      el.style.background = '';
      el.style.color = '';
      el.style.cursor = '';
      el.placeholder = id === 'order-rua' ? 'Ex: Av. Raul Pompéia'
        : id === 'order-bairro' ? 'Ex: Vila Bela'
          : 'Ex: Guaratinguetá / SP';
    });

    // Exibe todos os campos de endereço para preenchimento manual
    document.getElementById('addr-rua-group').style.display = 'block';
    document.getElementById('addr-bairro-cidade-group').style.display = 'grid';
    document.getElementById('addr-numero-group').style.display = 'block';
    document.getElementById('addr-ref-group').style.display = 'block';
  }
}

function resetCEPFields() {
  // Limpa valores
  ['order-rua', 'order-bairro', 'order-cidade', 'order-numero', 'order-reference'].forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    el.value = '';
    // Restaura estilo readonly caso o fallback manual os tenha tornado editáveis
    if (['order-rua', 'order-bairro', 'order-cidade'].includes(id)) {
      el.setAttribute('readonly', '');
      el.style.background = '#f0f7fc';
      el.style.color = 'var(--gray)';
      el.style.cursor = 'default';
      el.placeholder = '';
    }
  });
  // Esconde grupos de endereço
  ['addr-rua-group', 'addr-numero-group', 'addr-ref-group'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.style.display = 'none';
  });
  const bg = document.getElementById('addr-bairro-cidade-group');
  if (bg) bg.style.display = 'none';
  // Reseta ícones de status
  document.getElementById('cep-ok').style.display = 'none';
  document.getElementById('cep-error').style.display = 'none';
  document.getElementById('cep-msg').style.display = 'none';
}

// Observador de Revelação (Animação de Entrada)
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) e.target.classList.add('visible');
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
} else {
  // Fallback: exibe todos os elementos imediatamente
  document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
}
