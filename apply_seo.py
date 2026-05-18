import sys

new_head = """<!DOCTYPE html>
<html lang="pt-BR" prefix="og: https://ogp.me/ns#">
<head>
<meta charset="UTF-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="icon" type="image/png" href="img/logo.png" />

<!-- ════════════════════════════════════════════
     SEO PRIMÁRIO
════════════════════════════════════════════ -->
<title>Barbosa Restaurante | Churrasco em Guaratinguetá – Marmitex, Costela e Mais</title>
<meta name="description" content="Barbosa Restaurante em Guaratinguetá, SP. O melhor churrasco do Vale do Paraíba! Marmitex P, M e G com costela desossada, parmegiana de carne, frango grelhado e muito mais. Peça pelo WhatsApp com entrega rápida."/>
<meta name="keywords" content="restaurante guaratinguetá, churrasco guaratinguetá, marmitex guaratinguetá, barbosa restaurante, almoço guaratinguetá, marmita churrasco guaratinguetá, parmegiana guaratinguetá, costela guaratinguetá, frango grelhado guaratinguetá, comida vale do paraíba, delivery guaratinguetá, marmitex delivery, almoço delivery guaratinguetá, comida boa guaratinguetá"/>
<meta name="author" content="Barbosa Restaurante"/>
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"/>
<meta name="googlebot" content="index, follow"/>
<meta name="theme-color" content="#6EB5E0"/>
<meta name="mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="apple-mobile-web-app-title" content="Barbosa Restaurante"/>
<meta name="format-detection" content="telephone=yes"/>
<link rel="canonical" href="https://barbosarestaurante.com.br/"/>

<!-- ════════════════════════════════════════════
     GEO / LOCAL SEO
════════════════════════════════════════════ -->
<meta name="geo.region" content="BR-SP"/>
<meta name="geo.placename" content="Guaratinguetá, São Paulo, Brasil"/>
<meta name="geo.position" content="-22.8197;-45.1928"/>
<meta name="ICBM" content="-22.8197, -45.1928"/>

<!-- ════════════════════════════════════════════
     OPEN GRAPH (Facebook, WhatsApp, LinkedIn)
════════════════════════════════════════════ -->
<meta property="og:type" content="restaurant"/>
<meta property="og:site_name" content="Barbosa Restaurante"/>
<meta property="og:title" content="Barbosa Restaurante | Melhor Churrasco em Guaratinguetá – SP"/>
<meta property="og:description" content="O melhor churrasco do Vale do Paraíba! Marmitex P, M e G com costela desossada, parmegiana de carne e frango grelhado. Peça agora pelo WhatsApp e receba em casa."/>
<meta property="og:url" content="https://barbosarestaurante.com.br/"/>
<meta property="og:image" content="https://barbosarestaurante.com.br/img/logo.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:image:alt" content="Barbosa Restaurante – Churrasco em Guaratinguetá"/>
<meta property="og:locale" content="pt_BR"/>
<meta property="og:phone_number" content="+5512991136258"/>
<meta property="business:contact_data:locality" content="Guaratinguetá"/>
<meta property="business:contact_data:region" content="São Paulo"/>
<meta property="business:contact_data:country_name" content="Brasil"/>

<!-- ════════════════════════════════════════════
     TWITTER CARD
════════════════════════════════════════════ -->
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Barbosa Restaurante | Churrasco em Guaratinguetá"/>
<meta name="twitter:description" content="Marmitex P, M e G com o melhor churrasco do Vale do Paraíba. Costela desossada, parmegiana de carne e muito mais. Peça pelo WhatsApp!"/>
<meta name="twitter:image" content="https://barbosarestaurante.com.br/img/logo.png"/>
<meta name="twitter:image:alt" content="Barbosa Restaurante – Churrasco em Guaratinguetá"/>

<!-- ════════════════════════════════════════════
     SCHEMA.ORG — RESTAURANT (Rich Results Google)
════════════════════════════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://barbosarestaurante.com.br/#restaurant",
  "name": "Barbosa Restaurante",
  "alternateName": ["Barbosa Churrasco", "Barbosa Marmitex", "Restaurante Barbosa Guaratinguetá"],
  "description": "O melhor churrasco do Vale do Paraíba. Marmitex com costela desossada, parmegiana de carne, frango grelhado e kit churrasco. Delivery em Guaratinguetá e região.",
  "url": "https://barbosarestaurante.com.br",
  "telephone": "+5512991136258",
  "email": "contato@barbosarestaurante.com.br",
  "image": "https://barbosarestaurante.com.br/img/logo.png",
  "logo": "https://barbosarestaurante.com.br/img/logo.png",
  "priceRange": "R$20–R$35",
  "servesCuisine": ["Churrasco", "Comida Brasileira", "Parmegiana", "Frango Grelhado"],
  "hasMenu": "https://barbosarestaurante.com.br/#cardapio",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Avenida Raul Pompéia, 402, Vila Bela",
    "addressLocality": "Guaratinguetá",
    "addressRegion": "SP",
    "postalCode": "12500-000",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -22.8197,
    "longitude": -45.1928
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
      "opens": "11:00",
      "closes": "22:00"
    }
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+5512991136258",
    "contactType": "customer service",
    "availableLanguage": "Portuguese",
    "contactOption": "TollFree"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Cardápio Barbosa Restaurante",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Marmita de Churrasco",
          "description": "Carne bovina grelhada na brasa com acompanhamentos. Tamanho P, M ou G.",
          "offers": [
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"35.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Costela Desossada",
          "description": "Costela bovina macia, desossada e assada lentamente.",
          "offers": [
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"35.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Parmegiana de Carne",
          "description": "Carne bovina empanada com molho de tomate e queijo derretido.",
          "offers": [
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"35.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Parmegiana de Frango",
          "description": "Frango empanado com molho de tomate e queijo gratinado.",
          "offers": [
            {"@type":"Offer","price":"20.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Kit Churrasco",
          "description": "Mix das melhores carnes no espeto, direto da brasa.",
          "offers": [
            {"@type":"Offer","price":"100.00","priceCurrency":"BRL","name":"4 Pessoas"},
            {"@type":"Offer","price":"150.00","priceCurrency":"BRL","name":"6 Pessoas"},
            {"@type":"Offer","price":"200.00","priceCurrency":"BRL","name":"8 Pessoas"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Frango Grelhado",
          "description": "Peito de frango grelhado, temperado e suculento.",
          "offers": [
            {"@type":"Offer","price":"20.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Frango à Milanesa",
          "description": "Frango empanado crocante por fora, macio por dentro.",
          "offers": [
            {"@type":"Offer","price":"20.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "MenuItem",
          "name": "Filé de Peixe",
          "description": "Filé fresco grelhado, levinho e saboroso.",
          "offers": [
            {"@type":"Offer","price":"20.00","priceCurrency":"BRL","name":"Pequena"},
            {"@type":"Offer","price":"25.00","priceCurrency":"BRL","name":"Média"},
            {"@type":"Offer","price":"30.00","priceCurrency":"BRL","name":"Grande"}
          ]
        }
      }
    ]
  },
  "amenityFeature": [
    {"@type":"LocationFeatureSpecification","name":"Delivery","value":true},
    {"@type":"LocationFeatureSpecification","name":"Retirada no local","value":true},
    {"@type":"LocationFeatureSpecification","name":"Comer no estabelecimento","value":true},
    {"@type":"LocationFeatureSpecification","name":"Pedido via WhatsApp","value":true}
  ],
  "sameAs": [
    "https://wa.me/5512991136258",
    "https://www.google.com/maps?q=Avenida+Raul+Pomp%C3%A9ia,402,Vila+Bela,Guaratinguet%C3%A1,SP"
  ]
}
</script>

<!-- ════════════════════════════════════════════
     SCHEMA — LOCAL BUSINESS (reforço local SEO)
════════════════════════════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://barbosarestaurante.com.br/#localbusiness",
  "name": "Barbosa Restaurante",
  "description": "Restaurante especializado em churrasco em Guaratinguetá, SP. Delivery de marmitex com costela desossada, parmegiana e frango grelhado.",
  "url": "https://barbosarestaurante.com.br",
  "telephone": "+5512991136258",
  "priceRange": "$$",
  "image": "https://barbosarestaurante.com.br/img/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Avenida Raul Pompéia, 402, Vila Bela",
    "addressLocality": "Guaratinguetá",
    "addressRegion": "SP",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": -22.8197,
    "longitude": -45.1928
  },
  "areaServed": [
    {"@type":"City","name":"Guaratinguetá"},
    {"@type":"City","name":"Aparecida"},
    {"@type":"City","name":"Lorena"},
    {"@type":"City","name":"Cachoeira Paulista"},
    {"@type":"City","name":"Pindamonhangaba"}
  ],
  "openingHours": ["Mo-Su 11:00-22:00"],
  "servesCuisine": "Brazilian",
  "hasMap": "https://maps.google.com/?q=Avenida+Raul+Pompeia,402,Vila+Bela,Guaratingueta,SP"
}
</script>

<!-- ════════════════════════════════════════════
     SCHEMA — FAQ (aparece como rich result no Google)
════════════════════════════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "O Barbosa Restaurante faz delivery em Guaratinguetá?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim! O Barbosa Restaurante faz delivery em Guaratinguetá e região. Basta acessar o site, montar seu pedido e enviar pelo WhatsApp (12) 99113-6258. A taxa de entrega é calculada no WhatsApp."
      }
    },
    {
      "@type": "Question",
      "name": "Qual o cardápio do Barbosa Restaurante?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "O cardápio inclui: Marmita de Churrasco, Kit Churrasco, Costela Desossada, Parmegiana de Carne, Parmegiana de Frango, Frango Grelhado, Frango à Milanesa e Filé de Peixe. Disponível todos os dias em tamanhos P, M e G."
      }
    },
    {
      "@type": "Question",
      "name": "Quais os preços do Barbosa Restaurante?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pratos com frango, peixe ou parmegiana de frango: R$20 (P), R$25 (M), R$30 (G). Churrasco e pratos com carne bovina: R$25 (P), R$30 (M), R$35 (G). Kit Churrasco de R$100 a R$200. Bebidas a partir de R$7,00."
      }
    },
    {
      "@type": "Question",
      "name": "O Barbosa Restaurante tem opção para comer no local?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim! Além de delivery e retirada, o Barbosa Restaurante oferece a opção de comer no estabelecimento. Endereço: Av. Raul Pompéia, 402, Vila Bela - Guaratinguetá, SP."
      }
    },
    {
      "@type": "Question",
      "name": "Como fazer pedido no Barbosa Restaurante?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "É muito simples: acesse o site, escolha seu prato, o tamanho (P, M ou G), adicione bebidas, informe o tipo de pedido e clique em 'Enviar Pedido'. Você será redirecionado ao WhatsApp do restaurante com tudo preenchido automaticamente."
      }
    },
    {
      "@type": "Question",
      "name": "Qual o telefone do Barbosa Restaurante?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "O telefone e WhatsApp do Barbosa Restaurante é (12) 99113-6258."
      }
    },
    {
      "@type": "Question",
      "name": "O Barbosa Restaurante é aberto todos os dias?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim! O Barbosa Restaurante funciona todos os dias, com o cardápio completo disponível no almoço e jantar."
      }
    }
  ]
}
</script>

<!-- ════════════════════════════════════════════
     SCHEMA — BREADCRUMB
════════════════════════════════════════════ -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Início",
      "item": "https://barbosarestaurante.com.br/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Cardápio",
      "item": "https://barbosarestaurante.com.br/#cardapio"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Bebidas",
      "item": "https://barbosarestaurante.com.br/#bebidas"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "Localização",
      "item": "https://barbosarestaurante.com.br/#localizacao"
    }
  ]
}
</script>

<!-- ════════════════════════════════════════════
     PERFORMANCE & PRELOADS
════════════════════════════════════════════ -->
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="dns-prefetch" href="https://maps.googleapis.com"/>
<link rel="dns-prefetch" href="https://wa.me"/>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet"/>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace everything from <!DOCTYPE html> down to `<style>`
# But preserve everything from `<style>` onwards
parts = content.split('<style>')
if len(parts) >= 2:
    new_content = new_head + '\n<style>' + '<style>'.join(parts[1:])
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SEO Head successfully applied!")
else:
    print("Error: Could not find <style> tag to split the file.")

