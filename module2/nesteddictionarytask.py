students = {
    'id': [],
    'name': [],
    'city': []
}

n = int(input("Enter number of students: "))

for i in range(n):
    sid = int(input("Enter student ID: "))
    sname = input("Enter student Name: ")
    scity = input("Enter student City: ")

    students['id'].append(sid)
    students['name'].append(sname)
    students['city'].append(scity)

print("Student Data:")
print(students)