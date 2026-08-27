days=int(input("Enter the days:"))

match days:
    case 1:
        print("Monday ya somwar")
    case 2:
        print("Tuesday ya mangalwar")
    case 3:
        print("Wednesday ya budwar")
    case 4:
        print("Thursday ya guruwar")
    case 5:
        print("Friday ya shukrawar")
    case 6:
        print("Saturday ya shaniwar")
    case 7:
        print("Sunday ya ravivar")
    case _:
        print("Invalid input")