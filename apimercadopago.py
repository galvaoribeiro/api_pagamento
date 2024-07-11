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
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
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
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
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
            },
            "back_url": "https://www.mercadopago.com.co/subscriptions",
        }
    ]

    ids_planos = []
    for plano in planos:
        print(f'plano: {plano}')
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



