from flask import Flask
from app.config import Config
from app.routes.pages import pages_bp
from app.routes.api import api_bp
from app.extensions import get_db

def init_db(app):
    with app.app_context():
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT UNIQUE NOT NULL,
                setor TEXT NOT NULL,
                ultimo_preco NUMERIC DEFAULT 0
            );
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS compras (
                id SERIAL PRIMARY KEY,
                produto_id INTEGER REFERENCES produtos(id) ON DELETE CASCADE,
                quantidade NUMERIC DEFAULT 1,
                preco NUMERIC DEFAULT 0,
                comprado BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        cur.close()
        conn.close()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp)

    try:
        init_db(app)
    except Exception as e:
        print("Erro ao inicializar banco:", e)

    return app
