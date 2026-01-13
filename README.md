Visualize a aplicação real através do link no final deste README.md.

---

## 🔹 Stack
- Python 3.11+
- Flask 2.3+
- PostgreSQL
- HTML / CSS / JavaScript
- Cloud (Railway)

---

## 🔹 Estrutura do projeto

```
supermarket-system/
├─ app/
│   ├─ __init__.py            # create_app()
│   ├─ config.py              # Config / env
│   ├─ extensions.py          # DB (psycopg, etc)
│   │
│   ├─ routes/
│   │   ├─ __init__.py        # registra blueprints
│   │   ├─ pages.py           # rotas HTML
│   │   └─ api.py             # rotas REST (JSON)
│   │
│   ├─ services/              # regras de negócio
│   │   └─ __init__.py        # pacote services (NÃO blueprint)
│   │
│   ├─ repositories/          # acesso ao banco (SQL)
│   │   └─ __init__.py        # pacote repositories
│   │
│   ├─ templates/             # Jinja2
│   │   ├─ base.html
│   │   ├─ home.html
│   │   ├─ menu.html
│   │   └─ produtos.html
│   │
│   └─ static/                # arquivos estáticos
│       ├─ css/
│       │   └─ style.css
│       ├─ js/
│       │   └─ main.js
│       ├─ images/
│       │   └─ ...
│       └─ fonts/
│           └─ inter.woff2
│
├─ migrations/                # Alembic / Flask-Migrate
├─ tests/                     # pytest
├─ run.py                     # entrypoint da aplicação
├─ requirements.txt
├─ Procfile                   # Railway
├─ README.md
├─ .env                       # NÃO versionar
├─ .gitignore
└─ pyproject.toml             # opcional
```
---

## 📁 Como Rodar

```bash
pip install -r requirements.txt
python run.py
```
---

## 🔗 Acesso ao Sistema (Deploy)

O sistema está disponível online pelo Railway:

➡️ ** não disponível **

---

## 👨‍💻 Autor

* Desenvolvido por **Eduardo Libório**
* 📧 [eduardosoleno@protonmail.com](mailto:eduardosoleno@protonmail.com)

---