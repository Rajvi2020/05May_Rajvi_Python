age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible because weight is less than 50 kg.")
else:
    print("You are not eligible because age is below 18.")