import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Marquee CSS replacement
old_css_highlights = """  .highlights{background:var(--navy);padding:20px 24px}
  .highlights-inner{max-width:1100px;margin:0 auto;display:flex;gap:8px;overflow-x:auto;padding-bottom:4px}
  .highlights-inner::-webkit-scrollbar{display:none}"""

new_css_highlights = """  @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
  .highlights{background:var(--navy);padding:16px 0;overflow:hidden;border-bottom:1px solid rgba(110,181,224,.1);position:relative;}
  .highlights::after{content:'';position:absolute;top:0;right:0;bottom:0;width:60px;background:linear-gradient(to left, var(--navy), transparent);pointer-events:none;}
  .highlights::before{content:'';position:absolute;top:0;left:0;bottom:0;width:60px;background:linear-gradient(to right, var(--navy), transparent);pointer-events:none;z-index:2;}
  .highlights-inner{display:flex;gap:12px;width:max-content;animation:marquee 25s linear infinite;padding-bottom:0;}
  .highlights-inner:hover{animation-play-state:paused;}"""

content = content.replace(old_css_highlights, new_css_highlights)

# 2. Add cubic-bezier transition to menu cards
content = content.replace("transition:transform .3s,box-shadow .3s;", "transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;")
content = content.replace("transition:transform .3s, box-shadow .3s;", "transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;")

# 3. Add cubic-bezier to buttons and pill interactions
content = content.replace("transition:all .2s;", "transition:all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);")
content = content.replace("transition:background .2s;", "transition:background 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);")

# 4. Media query updates for better mobile
old_media = """  @media(max-width:768px){nav{padding:0 16px}.nav-links{display:none}.loc-wrap{grid-template-columns:1fr;gap:32px}.bar-inner{gap:10px}.bar-send span{display:none}section{padding:56px 16px}}"""

new_media = """  @media(max-width:768px){
    nav{padding:0 16px;height:60px;}
    .nav-links{display:none}
    .hero{padding:70px 16px 50px;}
    .hero h1{font-size:14vw;}
    .hero-sub{font-size:1.05rem;}
    .loc-wrap{grid-template-columns:1fr;gap:32px}
    .bar-inner{gap:10px;}
    .bar-send{padding:12px 18px;}
    .bar-send span{display:none}
    .bar-total{font-size:1.5rem;}
    section{padding:48px 16px}
    .modal-content{padding:20px 16px; border-radius:24px 24px 0 0;}
    .cart-item{padding:16px 0;}
    .cart-item-title{font-size:1rem;}
  }"""

content = content.replace(old_media, new_media)

# 5. HTML Highlights Duplication
old_html_highlights = """<div class="highlights">
  <div class="highlights-inner">
    <div class="hl-chip"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg> Carnes Premium</div>
    <div class="hl-chip">🔥 Churrasco Todo Dia</div>
    <div class="hl-chip">🥩 Kit Churrasco Especial</div>
    <div class="hl-chip">🦴 Costela Desossada</div>
    <div class="hl-chip">🚀 Entrega Rápida</div>
    <div class="hl-chip">📦 Marmitex P, M e G</div>
    <div class="hl-chip">🍗 Frango Grelhado Diário</div>
  </div>
</div>"""

new_html_highlights = """<div class="highlights">
  <div class="highlights-inner">
    <!-- Set 1 -->
    <div class="hl-chip"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg> Carnes Premium</div>
    <div class="hl-chip">🔥 Churrasco Todo Dia</div>
    <div class="hl-chip">🥩 Kit Churrasco Especial</div>
    <div class="hl-chip">🦴 Costela Desossada</div>
    <div class="hl-chip">🚀 Entrega Rápida</div>
    <div class="hl-chip">📦 Marmitex P, M e G</div>
    <div class="hl-chip">🍗 Frango Grelhado Diário</div>
    <!-- Set 2 -->
    <div class="hl-chip"><svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg> Carnes Premium</div>
    <div class="hl-chip">🔥 Churrasco Todo Dia</div>
    <div class="hl-chip">🥩 Kit Churrasco Especial</div>
    <div class="hl-chip">🦴 Costela Desossada</div>
    <div class="hl-chip">🚀 Entrega Rápida</div>
    <div class="hl-chip">📦 Marmitex P, M e G</div>
    <div class="hl-chip">🍗 Frango Grelhado Diário</div>
  </div>
</div>"""

content = content.replace(old_html_highlights, new_html_highlights)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Animations and Mobile optimizations applied.")
