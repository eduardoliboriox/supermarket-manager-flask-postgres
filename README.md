Visualize a aplicação real através do link no final deste README.md.

---

## 🔹 Tecnologias

- Python 3.11+
- Flask 2.3+
- SQLite (banco de dados local)
- HTML5, CSS3, Bootstrap 5
- DataTables (via CDN)
- JavaScript (Fetch API + AJAX)

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
│   ├─ repositories/     # SQL / ORM
│   ├─ templates/
│   └─ static/
│
├─ migrations/            # Alembic / Flask-Migrate
├─ tests/                 # pytest
│
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
python app.py
```

---

## 🔗 Acesso ao Sistema (Deploy)

O sistema está disponível online pelo Render:
Uso contramedidas até na versão free para a página não fechar por inatividade, caso feche, aguarde 50 segundos.

➡️ ** **

---

## 👨‍💻 Autor

* Desenvolvido por **Eduardo Libório**
* 📧 [eduardosoleno@protonmail.com](mailto:eduardosoleno@protonmail.com)

---