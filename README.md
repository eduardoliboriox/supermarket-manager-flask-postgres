## 🛒 Lista de Compras Inteligente

A Lista de Compras Inteligente é uma aplicação web desenvolvida para organizar compras domésticas de forma prática, visual e persistente, permitindo controlar quantidades, preços, totais, gasto previsto e saldo disponível em tempo real.
O sistema substitui listas em papel ou anotações improvisadas, oferecendo uma experiência fluida tanto no desktop quanto no mobile, com foco em simplicidade, organização e usabilidade.

---

## 🎯 Objetivo do Projeto
* Centralizar todos os produtos da compra em um único local
* Controlar valores automaticamente conforme as quantidades variam
* Manter os dados salvos mesmo após atualizar a página
* Facilitar o cadastro rápido de novos produtos
* Garantir uma experiência intuitiva e funcional

---

```
## 📁 Estrutura do Projeto
supermarket-system/
├─ app/
│   ├─ __init__.py            # Application Factory (create_app)
│   ├─ config.py              # Configurações e variáveis de ambiente
│   ├─ extensions.py          # Conexão com PostgreSQL
│   │
│   ├─ routes/
│   │   ├─ __init__.py
│   │   ├─ pages.py           # Rotas HTML
│   │   └─ api.py             # Rotas REST (JSON)
│   │
│   ├─ services/              # Regras de negócio
│   │   └─ __init__.py
│   │
│   ├─ repositories/          # Acesso ao banco (SQL)
│   │   └─ __init__.py
│   │
│   ├─ templates/
│   │   ├─ base.html
│   │   ├─ home.html
│   │   ├─ produtos.html
│   │   └─ menu.html
│   │
│   └─ static/
│       ├─ css/
│       │   └─ style.css
│       ├─ js/
│       │   └─ main.js
│       └─ images/
│
├─ migrations/                # Migrações (futuro)
├─ tests/                     # Testes automatizados
├─ run.py                     # Entry point da aplicação
├─ requirements.txt
├─ Procfile                   # Deploy (Railway)
├─ .env                       # Variáveis de ambiente (não versionar)
├─ .gitignore
└─ README.md
```
---

## 🚀 Funcionalidades
### 1. Cadastro de produtos por categoria:

* Alimentos Principais
* Complementos
* Temperos
* Higiene e Limpeza

### 2. Ajuste de quantidade com botões + / −

* Edição rápida de preço direto na tela
* Cálculo automático de:
* Total atual da compra
* Gasto previsto
* Saldo disponível

* Persistência automática dos dados usando LocalStorage
* Botão para limpar todos os dados da compra
* Modal para cadastro rápido de produtos
* Interface moderna e organizada
* Layout responsivo para desktop e mobile

---

## 🧮 Cálculo em Tempo Real
O sistema recalcula automaticamente:

* Total de cada produto (preço × quantidade)
* Total geral da compra
* Saldo disponível com base no gasto previsto informado
* Qualquer alteração de preço, quantidade ou orçamento reflete instantaneamente nos valores exibidos.

---

## 💾 Persistência de Dados
### 1. A aplicação salva automaticamente no navegador:

* Quantidade dos produtos
* Preços atualizados
* Gasto previsto
* Isso garante que os dados não sejam perdidos ao atualizar a página, permitindo continuar a compra de onde parou.

---

## 🪟 Modal de Cadastro de Produto
### 1. O cadastro de novos produtos é feito através de um modal simples, permitindo:

* Informar nome do produto
* Definir preço
* Selecionar a categoria
* Após salvar, o produto aparece automaticamente na lista correspondente.

---

## 🎨 Interface e Experiência do Usuário (UX)
* Design limpo e focado no conteúdo
* Botões grandes e acessíveis
* Separação clara por categorias
* Destaque visual para valores importantes
* Botão de ação destrutiva (Limpar dados) com cor diferenciada
* Interações sem recarregar a página

---

## 📱 Desktop e Mobile
### 💻 Desktop
* Visual completo
* Organização clara das categorias
* Ideal para planejamento detalhado

### 📲 Mobile
* Layout adaptado ao toque
* Navegação simples
* Experiência semelhante a aplicativo

## ⚙️ Tecnologias Utilizadas
* Python (Flask)
* HTML5
* CSS3
* JavaScript (Vanilla)
* Jinja2
* LocalStorage

---
```
## ▶️ Como Rodar o Projeto
pip install -r requirements.txt
python app.py
Depois, acesse no navegador:

http://127.0.0.1:5000
```
---

## 📌 Observações
* O sistema não utiliza login
* Os dados da compra atual ficam salvos localmente no navegador
* O cadastro de produtos é persistido no banco de dados
* Projeto ideal para uso pessoal ou familiar

---

## 👨‍💻 Autor 
Desenvolvido por Eduardo Libório
📧 eduardosoleno@protonmail.com  
