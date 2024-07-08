import mercadopago

def criar_planos():
    sdk = mercadopago.SDK("APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525")

    planos = [
        {
            "reason": "Plano Starter",
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 50,
                "currency_id": "BRL",
                "repetitions": 12,
                "free_trial": {
                    "frequency": 1,
                    "frequency_type": "months"
                },
                "back_url": "https://web-production-190ab.up.railway.app/assinatura_concluida",
                "auto_recurring_type": "regular"
            }
        },
        {
            "reason": "Plano Advanced",
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 100,
                "currency_id": "BRL",
                "repetitions": 12,
                "free_trial": {
                    "frequency": 1,
                    "frequency_type": "months"
                },
                "back_url": "https://web-production-190ab.up.railway.app/assinatura_concluida",
                "auto_recurring_type": "regular"
            }
        },
        {
            "reason": "Plano Premium",
            "auto_recurring": {
                "frequency": 1,
                "frequency_type": "months",
                "transaction_amount": 150,
                "currency_id": "BRL",
                "repetitions": 12,
                "free_trial": {
                    "frequency": 1,
                    "frequency_type": "months"
                },
                "back_url": "https://web-production-190ab.up.railway.app/assinatura_concluida",
                "auto_recurring_type": "regular"
            }
        }
    ]

    ids_planos = []
    for plano in planos:
        result = sdk.plan().create(plano)
        resposta = result['response']
        print(f'resposta é: {resposta}')
        if 'id' in result['response']:
            plano_id = result['response']['id']
            ids_planos.append(plano_id)
            print(f'Plano "{plano["reason"]}" criado com ID: {plano_id}')
        else:
            raise ValueError("A resposta da API do Mercado Pago não contém um campo 'id'.")

    return ids_planos

# Executar a criação dos planos e imprimir os IDs
if __name__ == "__main__":
    ids_planos = criar_planos()
    print("IDs dos planos criados:", ids_planos)


def criar_assinatura(user_id, plan_id):
    sdk = mercadopago.SDK("APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525")

    subscription_data = {
        "preapproval_plan_id": plan_id,
        "payer_email": "test_user_123456@testuser.com",
        "card_token_id": "CARD_TOKEN",  # Substitua por um token de cartão válido
        "back_url": "https://web-production-190ab.up.railway.app/assinatura_concluida",
        "reason": "Assinatura Premium",
        "external_reference": f"user_{user_id}"
    }

    result = sdk.preapproval().create(subscription_data)
    subscription = result["response"]
    print(f'criação da assinatura: {subscription}')
    
    # Verifique se o campo 'id' está presente na resposta
    if 'id' in subscription:
        return subscription["id"]
    else:
        raise ValueError("A resposta da API do Mercado Pago não contém um campo 'id'.")
