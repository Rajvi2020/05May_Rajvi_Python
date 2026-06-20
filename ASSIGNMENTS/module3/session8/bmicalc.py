import math
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))
bmi = weight / math.pow(height, 2)
print("BMI =", round(bmi, 2))