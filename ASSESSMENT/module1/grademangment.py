def calculate_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "Fail"

# Loop
while True:

    print("\nGrade Management System")
    print("1. Enter Marks")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '2':
        print("Exiting Program...")
        break

    elif choice == '1':

        marks = float(input("Enter student marks: "))

        grade = calculate_grade(marks)

        print("Grade:", grade)

    else:
        print("Invalid Choice")