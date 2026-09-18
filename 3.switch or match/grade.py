percentage=float(input("Enter the your percentage: "))

match percentage:
    case percentage if percentage >= 90:
        print("You have received an A grade,excellent work!")
    case percentage if percentage >= 80:
        print("You have received a B grade,good job!")
    case percentage if percentage >= 70:
        print("You have received a C grade,keep it up!")
    case percentage if percentage >= 60:
        print("You have received a D grade, you need to improve.")
    case percentage if percentage < 60:
        print("You have received an E grade, you need to work harder.")

    case percentage if percentage < 50:
        print("You have received an F grade, you are failed , need to work harder.")

    case _:
        print("Invalid percentage. Please enter a valid percentage between 0 and 100.")