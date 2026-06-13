class PaymentFailedError(Exception):
    pass
def process_payment(amount):
    try:
        if amount <= 0:
            raise PaymentFailedError("Payment Failed!")
        else:
            print("Payment Successful")

    except PaymentFailedError as e:
        print(e)
process_payment(500)
process_payment(0)