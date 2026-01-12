from flask import Blueprint, request, jsonify
from app.extensions import get_db

api_bp = Blueprint("api", __name__, url_prefix="/api")

@api_bp.route("/produto/excluir", methods=["POST"])
def excluir_produto():
    data = request.get_json()

    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM produtos WHERE id=%s", (data["id"],))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "ok"})


@api_bp.route("/produto/atualizar", methods=["POST"])
def atualizar_produto():
    data = request.get_json()

    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE produtos
        SET nome = %s,
            setor = %s,
            ultimo_preco = %s
        WHERE id = %s
    """, (
        data["nome"],
        data["setor"],
        data["preco"],
        data["id"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"status": "ok"})
