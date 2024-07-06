import mercadopago

def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-5966197263163161-070317-6ab5cace0b168a1161e2acb15eb3e35c-1883683525")

    payment_data = {
        "items": [
            {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99}
        ],
        "back_urls": {
            "success": "https://web-production-190ab.up.railway.app//compracerta",
            "failure": "https://web-production-190ab.up.railway.app//compraerrada",
            "pending": "https://web-production-190ab.up.railway.app//compraerrada",
        },
        "auto_return": "all"
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    #print(payment)
    link_iniciar_pagamento = payment["init_point"]
    return link_iniciar_pagamento