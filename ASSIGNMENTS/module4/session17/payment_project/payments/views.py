
from django.shortcuts import render,redirect

from .paytm_service import create_order, initiate_payment
import stripe
from django.conf import settings
def home(request):
    return render(request, "payments/home.html")



def food_success(request):
    return render(request, "payments/food_success.html")


def food_cancel(request):
    return render(request, "payments/food_cancel.html")



def pay(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        amount = request.POST.get("amount")

        payload = create_order(
            name,
            email,
            amount
        )

        response = initiate_payment(payload)

        txn_token = response["body"]["txnToken"]
        order_id = payload["body"]["orderId"]

        return render(request, "payments/paytm_redirect.html", {
            "mid": payload["body"]["mid"],
            "order_id": order_id,
            "txn_token": txn_token,
        })

    return render(request, "payments/pay.html")


import os
from django.shortcuts import render
from paytmchecksum import PaytmChecksum


id="m8v4cx"
def payment_callback(request):

    payment_data = request.POST.dict()

    merchant_key = os.getenv("PAYTM_MERCHANT_KEY")

    received_checksum = payment_data.pop(
        "CHECKSUMHASH",
        None
    )

    is_valid = PaytmChecksum.verifySignature(
        payment_data,
        merchant_key,
        received_checksum
    )

    if is_valid and payment_data.get("STATUS") == "TXN_SUCCESS":
        status = "success"
        message = "Payment Successful!"
    else:
        status = "failure"
        message = "Payment Failed!"

    return render(
        request,
        "payments/payment_callback.html",
        {
            "status": status,
            "message": message,
            "payment_data": payment_data,
        }
    )






def food_order(request):

    if request.method == "POST":

        dish_name = request.POST.get("dish_name")
        price = float(request.POST.get("price"))

        stripe.api_key = settings.STRIPE_SECRET_KEY

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "inr",
                        "product_data": {
                            "name": dish_name,
                        },
                        "unit_amount": int(price * 100),
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/food-success/",
            cancel_url="http://127.0.0.1:8000/food-cancel/",
        )

        return redirect(checkout_session.url)

    return render(request, "payments/food_order.html")





