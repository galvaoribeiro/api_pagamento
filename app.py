from flask import Flask, request, render_template
from apimercadopago import gerar_link_pagamento
import mercadopago
import json
import os

app = Flask(__name__)

# Inicialize o SDK do Mercado Pago
sdk = mercadopago.SDK("APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525")


@app.route("/")
def homepage():
    #print(f'entrei na homepage')
    user_id = "69"  # Exemplo de ID do usuário comprador
    link_iniciar_pagamento = gerar_link_pagamento(user_id)
    
    return render_template("homepage.html", link_pagamento=link_iniciar_pagamento)

@app.route("/compracerta")
def compra_certa():
    # Aqui estamos lendo o último pagamento do arquivo JSON para simulação
    if os.path.exists("payments.json"):
        with open("payments.json", "r") as payments_file:
            payments = payments_file.readlines()
            if payments:
                last_payment = json.loads(payments[-1])
                return render_template("compracerta.html", payment_info=last_payment)
    
    return render_template("compracerta.html", payment_info=None)

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    #print(f'dados na função webhook: {data}')
    if data:
        with open("webhook_logs.json", "a") as webhook_log:
            json.dump(data, webhook_log)
            webhook_log.write("\n")

        if data['action'] == 'payment.created':
            payment_id = data['data']['id']
            # Chame a API do Mercado Pago para obter os detalhes do pagamento
            payment = sdk.payment().get(payment_id)
            payment_info = payment['response']
            #print(f'retorno com sucesso das informações de pagamento: {payment_info}')
            # Processar informações do pagamento
            process_payment(payment_info)

    return '', 200

def process_payment(payment_info):
    # Função para processar e salvar informações do pagamento
    with open("payments.json", "a") as payments_file:
        json.dump(payment_info, payments_file)
        payments_file.write("\n")
        #print(f'escrevendo na função process payment')

    print(f"Pagamento recebido: {payment_info}")


if __name__ == "__main__":
    app.run()
