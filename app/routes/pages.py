from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import get_db

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def home():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, nome, setor, ultimo_preco
        FROM produtos
        ORDER BY setor, nome
    """)
    produtos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("home.html", produtos=produtos, page="home")


@pages_bp.route("/produtos")
def produtos():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, nome, ultimo_preco, setor
        FROM produtos
        ORDER BY setor, nome
    """)
    produtos = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("produtos.html", produtos=produtos, page="produtos")


@pages_bp.route("/add", methods=["POST"])
def add_item():
    nome = request.form["nome"]
    preco = float(request.form["preco"])
    setor = request.form["setor"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO produtos (nome, setor, ultimo_preco)
        VALUES (%s, %s, %s)
        ON CONFLICT (nome)
        DO UPDATE SET ultimo_preco = EXCLUDED.ultimo_preco
    """, (nome, setor, preco))

    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("pages.home"))
