try:
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    total = price * qty
    print("Total Order Amount:", total)
except ValueError:
    print("Error: Please enter numeric values only!")