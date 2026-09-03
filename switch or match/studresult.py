print("____ Student Result System ____")

name = input("Enter your name: ")
rollno = int(input("Enter your roll number: "))
marks = float(input("Enter your marks: "))

print("\n1. Enter student details")
print("2. View student details")
print("3. Calculate result")
print("4. Calculate grade")
print("5. Exit")

choice = int(input("Enter your choice (1-5): "))

match choice:

    case 1:
        print("\n----- STUDENT DETAILS ENTERED -----")
        print("Student details entered successfully!")

    case 2:
        print("\n----- STUDENT DETAILS -----")
        print("Name:", name)
        print("Roll Number:", rollno)
        print("Marks:", marks)

    case 3:
        print("\n----- STUDENT RESULT -----")

        if marks < 0 or marks > 100:
            print("Invalid marks.")
        elif marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

    case 4:
        print("\n----- STUDENT GRADE -----")

        if marks < 0 or marks > 100:
            print("Invalid marks.")
        elif marks >= 90:
            print("Grade: A+")
        elif marks >= 80:
            print("Grade: A")
        elif marks >= 70:
            print("Grade: B")
        elif marks >= 60:
            print("Grade: C")
        elif marks >= 40:
            print("Grade: D")
        else:
            print("Grade: F")

    case 5:
        print("\nThank you for using Student Result System.")

    case _:
        print("\nInvalid choice.")