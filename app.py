from flask import Flask, request, render_template, jsonify
import mercadopago
import os

app = Flask(__name__)

# IDs dos planos de assinatura previamente criados (substitua pelos IDs reais)
PLANO_STARTER_ID = "2c9380849082b3f601909fdd77ef0959"
PLANO_ADVANCED_ID = "2c9380849082b3b801909fdd7ad0095a"
PLANO_PREMIUM_ID = "2c9380849082b3f601909fdd7d82095a"

def criar_assinatura(user_id, plan_id, card_token):
    sdk = mercadopago.SDK(os.getenv("MERCADO_PAGO_ACCESS_TOKEN"))
    print(f'sdk: {sdk}')

    print(f'plan id in criar_assinatura: {plan_id}')

    subscription_data = {
        "preapproval_plan_id": plan_id,
        "payer_email": "test_user_123456@testuser.com",  # Substitua pelo email do comprador
        "card_token_id": card_token,  # Use o token recebido do frontend
        "back_url": "https://web-production-190ab.up.railway.app/assinatura_concluida",
        "reason": "Assinatura Premium",
        "external_reference": f"user_{user_id}"
    }

    try:
        result = sdk.subscription().create(subscription_data)
        subscription = result["response"]
        print(f'criação da assinatura: {subscription}')
        
        # Verifique se o campo 'id' está presente na resposta
        if 'id' in subscription:
            return subscription["id"]
        else:
            raise ValueError("A resposta da API do Mercado Pago não contém um campo 'id'.")
    except Exception as e:
        print(f'Erro ao criar assinatura: {e}')
        raise ValueError(f'Erro ao criar assinatura: {e}')

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/criar_assinatura", methods=["POST"])
def criar_assinatura_view():
    data = request.get_json()
    user_id = data.get("user_id")
    print(f'user: {user_id}')
    plan_id = data.get("plan_id")
    print(f'plan ID: {plan_id}')
    card_token = data.get("token")
    print(f'card token: {card_token}')
    
    if not user_id or not plan_id or not card_token:
        return "Dados incompletos", 400
    
    try:
        subscription_id = criar_assinatura(user_id, plan_id, card_token)
        print(f'subscription id: {subscription_id}')
        return jsonify({'subscription_id': subscription_id})
    except ValueError as e:
        return str(e), 400

@app.route("/assinatura_concluida")
def assinatura_concluida():
    return render_template("assinatura_concluida.html")

if __name__ == "__main__":
    os.environ["MERCADO_PAGO_ACCESS_TOKEN"] = "APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525"
    app.run()
