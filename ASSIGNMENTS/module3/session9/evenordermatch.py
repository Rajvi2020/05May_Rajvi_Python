import re

orders = ["ORD1234", "ORD5678", "ORD9999", "ORD0001"]

pattern = r"ORD\d*[02468]$"

for order in orders:
    if re.match(pattern, order):
        print(order)