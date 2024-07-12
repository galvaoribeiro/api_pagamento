import mercadopago

def gerar_link_pagamento(user_id):
    sdk = mercadopago.SDK("APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525")

    payment_data = {
        "items": [
            {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99},
            {"id": "2", "title": "short", "quantity": 1, "currency_id": "BRL", "unit_price": 49.99}
        ],

        "payer": {
           # "id": user_id,  # Adiciona o ID do usuário comprador
            #"email": "test_user_123456@testuser.com"
            "identification": {
      "type": "id_comprador",
      "number": user_id
    },
        },
        
        "back_urls": {
            "success": "https://web-production-190ab.up.railway.app/compracerta",
            "failure": "https://web-production-190ab.up.railway.app/compraerrada",
            "pending": "https://web-production-190ab.up.railway.app/compraerrada",
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]

    external_reference = f"user_{user_id}-{payment['id']}"
    payment['external_reference'] = external_reference
    payment_data['external_reference'] = external_reference

    # Atualizar a preferência com o external_reference
    sdk.preference().update(payment['id'], payment_data)
    
    print(f'criação da preferência de pagamento: {payment}')
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento