from flask import Flask, request, render_template
from apimercadopago import gerar_link_pagamento
#import mercadopago

app = Flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("homepage.html", link_pagamento=link_iniciar_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)
    return '', 200


if __name__ == "__main__":
    app.run()
