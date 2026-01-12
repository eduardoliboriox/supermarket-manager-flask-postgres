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
project/
├─ app/
│   ├─ __init__.py        # create_app()
│   ├─ config.py          # configs/env
│   ├─ extensions.py      # db
│   │
│   ├─ routes/
│   │   ├─ pages.py       # HTML
│   │   └─ api.py         # REST
│   │
│   ├─ services/          # regras de negócio
│   ├─ repositories/      # SQL / ORM
│   ├─ templates/
│   │   ├─ base.html
│   │   ├─ home.html
│   │   ├─ produtos.html
│   │   └─ menu.html
│   │
│   └─ static/
│       ├─ css/
│       │   └─ style.css
│       │
│       ├─ js/
│       │   └─ main.js
│       │  
│       ├─ images/
│       │   ├─ icons/
│       │   │  
│       │   ├─ users/
│       │   │   ├─ default.png
│       │   │   └─ user_123.jpg
│       │   │  
│       │   ├─ logos/
│       │   │   └─ logo.png
│       │   │  
│       │   └─ banners/
│       │       └─ hero.jpg
│       │  
│       └─ fonts/
│              └─ inter.woff2
│
├─ migrations/            # Alembic / Flask-Migrate
├─ tests/                 # pytest
├─ run.py                 # entrypoint da aplicação
├─ requirements.txt
├─ README.md              # documentação principal
├─ Procfile               # Railway / Heroku
├─ .env                   # variáveis locais (NÃO versionar)
├─ .gitignore
└─ pyproject.toml (opcional)
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

➡️ ** **

---

## 👨‍💻 Autor

* Desenvolvido por **Eduardo Libório**
* 📧 [eduardosoleno@protonmail.com](mailto:eduardosoleno@protonmail.com)

---