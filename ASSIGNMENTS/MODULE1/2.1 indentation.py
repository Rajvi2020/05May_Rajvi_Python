# Variables should use lowercase_with_underscores
student_name = "Rajvi"
student_marks = 85
# Function names should also use lowercase_with_underscores
def display_result():
    """Display student result."""

    # Proper indentation using 4 spaces
    if student_marks >= 35:
        print(student_name, "has passed the exam.")
    else:
        print(student_name, "has failed the exam.")
# Function call
display_result()
