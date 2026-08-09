
import uuid
import os
import requests
from paytmchecksum import PaytmChecksum


def create_order(name, email, amount):

    order_id = "IPL_" + str(uuid.uuid4())[:8]

    body = {
        "requestType": "Payment",
        "mid": os.getenv("PAYTM_MID"),
        "websiteName": os.getenv("PAYTM_WEBSITE"),
        "orderId": order_id,
        "callbackUrl": os.getenv("PAYTM_CALLBACK_URL"),
        "txnAmount": {
            "value": str(amount),
            "currency": "INR"
        },
        "userInfo": {
            "custId": email
        }
    }

    merchant_key = os.getenv("PAYTM_MERCHANT_KEY")

    checksum = PaytmChecksum.generateSignature(
        str(body),
        merchant_key
    )

    payload = {
        "head": {
            "signature": checksum
        },
        "body": body
    }

    return payload


def initiate_payment(payload):

    url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction"

    response = requests.post(
        url,
        json=payload,
        timeout=30
    )

    return response.json()
