days=int(input("Enter the number of days:"))

match days:
    case 31:
        print("the month name is january,march,may,july,august,october,december")
    case 30:
        print("the month name is april,june,september,november")
    case 28:
        print("the month name is february and it is february in non-leap year")

    case 29:
        print("the month name is february and it is february in leap year")
    case _:
        print("Invalid input. Please enter a valid number of days (28, 29, 30, or 31).")

    