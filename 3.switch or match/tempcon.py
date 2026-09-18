choice=int(input("Enter your choice(1-2): "))

match choice:
    case 1:
        celsius=float(input("Enter value in celsius:"))
        fahrenheit=(celsius*9/5)+32
        print(celsius,"C =",fahrenheit,"F")

    case 2:
        fahrenheit=float(input("Enter value in fahrenheit:"))
        celsius=(fahrenheit-32)*5/9
        print(fahrenheit,"F =",celsius,"C")

    case _:
        print("Invalid choice")