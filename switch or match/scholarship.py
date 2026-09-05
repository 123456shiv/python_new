print("===== STUDENT GRADE + SCHOLARSHIP =====")

print("\n1. Calculate Grade")
print("2. Check Scholarship")

choice = int(input("\nEnter your choice: "))

marks = float(input("Enter your marks: "))
attendance = float(input("Enter attendance percentage: "))

match choice:

    case 1:
        if marks >= 90:
            print("Grade: A")
        elif marks >= 80:
            print("Grade: B")
        elif marks >= 70:
            print("Grade: C")
        elif marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")

    case 2:
        if attendance < 75:
            print("No Scholarship")
            print("Reason: Attendance is below 75%")

        elif marks >= 90:
            print("Scholarship: 50%")

        elif marks >= 80:
            print("Scholarship: 30%")

        elif marks >= 70:
            print("Scholarship: 20%")

        else:
            print("No Scholarship")

    case _:
        print("Invalid choice!")