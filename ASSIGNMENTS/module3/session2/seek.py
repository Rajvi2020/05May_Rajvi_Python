def read_next_line(filename):
    file = open(filename, "r")
    file.seek(20)
    print(file.readline())
    file.close()

read_next_line("lyrics.txt")