print("____Banking Transaction System____")

balance=float(input("Enter your current balance:"))
print("1. balance inquiry")
print("2. deposit")
print("3. withdraw")
print("4. transfer")
print("5. exit")

choice=int(input("Enter your choice (1-4): "))

match choice:   
    case 1:
        print("\n ----balance inquiry succesfull --")
        print("Current balance: ₹",balance)

    case 2:
        deposit=float(input("Enter the amount to deposit: ₹"))

        if deposit <= 0:
            print("invalid deposit amount")
        else:
            balance = balance + deposit
            print("\nDeposit successful!")
            print("Current Balance: ₹", balance)

    case 3:
        withdraw = float(input("Enter withdrawal amount: ₹"))

        if withdraw <= 0:
            print("Invalid withdrawal amount.")
        elif withdraw > balance:
            print("\nInsufficient Balance!")
            print("Current Balance: ₹", balance)
        else:
            balance = balance - withdraw
            print("\nWithdrawal successful!")
            print("Current Balance: ₹", balance)

    case 4:
        print("\nThank you for using our banking service.")
        print("Current Balance: ₹", balance)

    case 5:
        print("\nThank you for using our banking service.")

    case _:
        print("\nInvalid choice.")