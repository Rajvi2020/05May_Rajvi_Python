file = open("orders.txt", "r")
line = file.readline()
while line:
    print(line.strip())
    print("Pointer position:", file.tell())
    line = file.readline()
file.close()

