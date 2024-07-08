from flask import Flask, request, render_template
from apimercadopago import criar_assinatura, criar_planos
import mercadopago

app = Flask(__name__)

# IDs dos planos de assinatura previamente criados
PLANO_STARTER_ID = "your_starter_plan_id"
PLANO_ADVANCED_ID = "your_advanced_plan_id"
PLANO_PREMIUM_ID = "your_premium_plan_id"

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/criar_assinatura", methods=["POST"])
def criar_assinatura_view():
    user_id = "123456789"  # Exemplo de ID do usuário comprador
    plano = request.form.get("plano")
    
    if plano == "starter":
        plan_id = PLANO_STARTER_ID
    elif plano == "advanced":
        plan_id = PLANO_ADVANCED_ID
    elif plano == "premium":
        plan_id = PLANO_PREMIUM_ID
    else:
        return "Plano inválido", 400

    try:
        subscription_id = criar_assinatura(user_id, plan_id)
        return f'Assinatura criada com ID: {subscription_id}'
    except ValueError as e:
        return str(e), 400

@app.route("/assinatura_concluida")
def assinatura_concluida():
    return render_template("assinatura_concluida.html")

if __name__ == "__main__":
    app.run()




'''

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(f'dados na função webhook: {data}')
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
'''