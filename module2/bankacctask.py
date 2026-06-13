def accopen(ac_no, ac_holdername, ac_type, balance=0):
    return [ac_no, ac_holdername, ac_type, balance]



x = accopen(101, "kishan", "saving", 0)


def deposit(amount):
    global x

    if amount < 2000:
        print("Deposit should be equal or greater than 2000")
    else:
        x[3] = x[3] + amount
        print("Deposited:", amount)

    return x[3]


def withdrawal(amount):
    global x

    if amount > x[3]:
        print("Balance insufficient")
    else:
        x[3] = x[3] - amount
        print("Amount withdrawn:", amount)

    return x[3]


def statement():
    global x

    print("Account Number:", x[0])
    print("Holder Name:", x[1])
    print("Account Type:", x[2])
    print("Balance:", x[3])


deposit(2500)
withdrawal(500)
statement()