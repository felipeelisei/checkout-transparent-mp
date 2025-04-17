from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import mercadopago


def checkout_transparente_view(request):
    sdk = mercadopago.SDK("SUBSTITUIR_PELA_SUA_ACCESS_KEY")
    preference_data = {
        "items": [
            {
                "title": "Plano Anual",
                "quantity": 1,
                "unit_price": 299.90,
                "currency_id": "BRL"
            }
        ],
        "back_urls": {
            "success": "http://127.0.0.1:8000/checkout/sucesso/",
            "failure": "http://127.0.0.1:8000/checkout/erro/",
            "pending": "http://127.0.0.1:8000/checkout/pendente/"
        },
        "auto_return": "approved",
        "payer_email": "comprador@example.com",
        "payer": {
            "name": "Comprador",
            "surname": "Exemplo",
            "email": "comprador@example.com"
        }
    }

    # Cria a preferência no Mercado Pago
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    # Passa a preferência para o template
    return render(request, 'checkout_transparente.html', {
        'preference_id': preference['id'],
        'public_key': 'SUBSTITUIR_PELA_SUA_PUBLIC_KEY',
    })


@csrf_exempt
def processar_pagamento(request):
    if request.method == 'POST':
        try:
            print("Recebendo dados do pagamento:", request.body)
            data = json.loads(request.body)
            print("Dados processados:", data)

            sdk = mercadopago.SDK("SUBSTITUIR_PELA_SUA_ACCESS_KEY")

            cardholder_name = data.get("cardholder_name", "APRO")
            
            # Preparar dados de pagamento
            payment_data = {
                "transaction_amount": float(data.get("amount", 0)),
                "token": data.get("token"),
                "description": "Plano Premium",
                "installments": int(data.get("installments", 1)),
                "payment_method_id": data.get("payment_method_id"),
                "payer": {
                    "email": data.get("email", "comprador@example.com"),
                    "identification": {
                        "type": data.get("doc_type", "CPF"),
                        "number": data.get("doc_number", "")
                    }
                }
            }
            
            # Adicionar issuer_id se existir
            if data.get("issuer_id"):
                payment_data["issuer_id"] = data.get("issuer_id")
            
            print("Enviando para o Mercado Pago:", payment_data)
            payment_response = sdk.payment().create(payment_data)
            print("Resposta do Mercado Pago:", payment_response)
            
            if payment_response.get("status") == 201:
                payment = payment_response["response"]
                status = payment.get("status")
                status_detail = payment.get("status_detail")
                
                return JsonResponse({
                    "status": status,
                    "status_detail": status_detail,
                    "payment_id": payment.get("id"),
                    "redirect_url": "/checkout/sucesso/" if status == "approved" else "/checkout/pendente/"
                })
            else:
                error_msg = payment_response.get("response", {}).get("message", "Erro desconhecido")
                return JsonResponse({"error": error_msg}, status=400)

        except Exception as e:
            print("Erro ao processar pagamento:", str(e))
            import traceback
            traceback.print_exc()  # Imprime o stack trace completo
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método não permitido"}, status=405)


def success_view(request):
    return render(request, 'success.html')


def failure_view(request):
    return render(request, 'failure.html')


def pending_view(request):
    return render(request, 'pending.html')
