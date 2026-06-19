import re
def is_valid_pnr(pnr):
    pattern = r"^\d{10}$"
    if re.match(pattern, pnr):
        return True
    else:
        return False
pnr = input("Enter PNR Number: ")
if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")