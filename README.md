# Barbosa Restaurante

Landing page profissional e moderna para o restaurante Barbosa em Guaratinguetá-SP. O site conta com design responsivo, animações de carregamento e otimização para SEO (Search Engine Optimization) para atrair clientes locais.

## Funcionalidades Principais

- **Design Moderno e Responsivo**: Interface adaptada para desktops, tablets e celulares.
- **SEO Otimizado**: Meta tags completas, dados estruturados (Schema.org) e palavras-chave relevantes para melhor posicionamento no Google.
- **Navegação Clean**: Menu fixo com link para o cardápio e botão de WhatsApp.
- **Seção de WhatsApp**: Botão flutuante e link direto no footer para pedidos rápidos.
- **Seção Cardápio Interativa**:
  - Tabs para filtrar por categoria (Marmitex, Pratos do Dia, Lanches).
  - Botões "Ver no WhatsApp" em cada item.
  - Modal com detalhes dos pratos (descrição, preço e opção de pedido).
- **Animações de Entrada**: Elementos deslizam suavemente para a tela ao rolar a página.
- **Formulário de Pedidos**:
  - Validação de CEP integrada com a API ViaCEP.
  - Auto-preenchimento de endereço.
  - Campos obrigatórios com validação visual.
- **Design System**:
  - Cores corporativas (Azul, Dourado e Branco).
  - Tipografia premium (`Cormorant Garamond` e `Jost`).

## Estrutura do Projeto

```
.                                      # Raiz do projeto
├── BarbosaRestaurante/                # Pasta do site estático
│   ├── css/                           # Arquivos CSS
│   │   ├── main.css                 # Estilos gerais e animações
│   │   └── custom-properties.css    # Variáveis de cores e tipografia
│   ├── fonts/                         # Fontes web personalizadas
│   ├── img/                           # Imagens e ícones
│   ├── js/                            # Arquivos JavaScript
│   │   ├── main.js                  # Lógica principal e interatividade
│   │   ├── form-handlers.js         # Validação de formulários e CEP
│   │   └── utils.js                 # Utilitários gerais (cep-lookup, reveal)
│   ├── index.html                     # Página principal (Homepage)
│   ├── README.md                      # Documentação do projeto
│   └── seo-audit.md                   # Relatório de auditoria SEO
```

## Como Executar

Como é um site estático, basta abrir o arquivo `index.html` em qualquer navegador moderno:

1. Navegue até a pasta `BarbosaRestaurante/`.
2. Dê um duplo clique em `index.html`.

## Tecnologias Utilizadas

- **HTML5**: Estrutura semântica.
- **CSS3**: Design moderno, Flexbox, Grid, animações CSS e variáveis.
- **JavaScript (Vanilla)**: Sem dependências externas para funcionalidades principais.
- **API ViaCEP**: Consulta de endereços pelo CEP.

## Otimizações de SEO

O site inclui:
- Título e descrição otimizados.
- Keywords relevantes para o nicho de restaurantes locais.
- Dados estruturados (JSON-LD) para o schema `Restaurant`.
- Tags Open Graph para mídias sociais.

## Licença

Este projeto foi desenvolvido sob demanda para o Barbosa Restaurante.

**Desenvolvido por [2TYPE/Filipe Andrade]**
