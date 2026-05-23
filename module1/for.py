# for i in range(1,6):
#     marks = int(input("Enter marks : "))
#     if marks > 70:
#         print("A grade")
#     else:
#         print("B grade")

# for i in range(6): # 0 -  5
#     print("Hello",end=" | ")

# lang=["python","Java"]
# feature=["Advance","Popular"]

# for a in lang:
#    for b in feature:
#        print(a,b)

for row in range(1,6):
    for col in range(1,6):
        if row == 3 and col == 3:
            print(" $ ",end=" ")
        else:
            print(" * ",end=" ")
    print()