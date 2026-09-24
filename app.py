import traceback

from flask import Flask, request, jsonify
from crew import executar_analise


app = Flask(__name__)


# ============================================================
# ROTA INICIAL
# ============================================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "online"
    })


# ============================================================
# ROTA DE ANÁLISE
# ============================================================

@app.route("/analisar", methods=["POST"])
def analisar():

    data = request.get_json(silent=True)

    # --------------------------------------------------------
    # VERIFICAÇÃO DO JSON
    # --------------------------------------------------------

    if data is None:

        return jsonify({
            "status": "error",
            "erro": "Nenhum JSON válido foi recebido."
        }), 400


    # --------------------------------------------------------
    # VERIFICAÇÃO DO CAMPO TEXT
    # --------------------------------------------------------

    if "text" not in data:

        return jsonify({
            "status": "error",
            "erro": "O parâmetro 'text' não foi informado."
        }), 400


    text = data["text"]


    # --------------------------------------------------------
    # VERIFICAÇÃO DO TIPO
    # --------------------------------------------------------

    if not isinstance(text, str):

        return jsonify({
            "status": "error",
            "erro": "O parâmetro 'text' deve ser textual."
        }), 400


    # --------------------------------------------------------
    # LOG
    # --------------------------------------------------------

    print("\n============================================")
    print("CONTEXTO RECEBIDO")
    print("============================================")
    print(text)
    print("============================================\n")


    # --------------------------------------------------------
    # EXECUÇÃO DO CREW
    # --------------------------------------------------------

    try:

        resultado = executar_analise(text)

    except Exception as e:

        print("\n============================================")
        print("ERRO NO CREW")
        print("============================================")
        traceback.print_exc()
        print("============================================\n")

        return jsonify({
            "status": "error",
            "erro": "Erro ao executar a análise.",
            "detalhes": str(e)
        }), 500


    # --------------------------------------------------------
    # RESPOSTA
    # --------------------------------------------------------

    return jsonify({
        "status": "success",
        "resultado": resultado
    })


# ============================================================
# INICIALIZAÇÃO
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )