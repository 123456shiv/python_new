choice=int(input("Enter your choice (1-5):"))
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

match choice:
    case 1:
        print(num1+num2)

    case 2:
        print(num1-num2)

    case 3:
        print(num1*num2)

    case 4:
        print(num1/num2)

    case 5:
        print(num1%num2)

    case _:
        print("Invalid input. Please enter a valid choice (1, 2, 3, 4, or 5)")