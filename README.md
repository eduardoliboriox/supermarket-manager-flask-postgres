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
Nome do Projeto/
├─ static/
│   ├─ logo.png 
│       ├─ css/
│            └─ style.css  
│       ├─ js/
│            └─ main.js  
├─ templates/
│  ├─ base.html
│  ├─ dashboard.html
│  ├─ index.html
├─ app.py
├─ x--banco
├─ ping.py
├─ Profile   
├─ README.md   
├─ requirements.txt 
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
│   └─ static/
│
├─ migrations/
├─ tests/
├─ run.py
├─ requirements.txt
└─ .env

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