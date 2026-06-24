class Payment:
    def pay(self, amount):
        print("Paying", amount)

class UPI(Payment):
    def pay(self, amount):
        print("Paying", amount, "via UPI")

p = Payment()
u = UPI()

p.pay(20000)
u.pay(20000)