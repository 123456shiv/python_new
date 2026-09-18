balance = int(input("Enter your initial balance: "))

print("\n----- ATM MENU -----")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("Your balance is:", balance)

    case 2:
        deposit = int(input("Enter deposit amount: "))
        balance = balance + deposit
        print("Your balance is:", balance)

    case 3:
        withdraw = int(input("Enter withdrawal amount: "))

        if withdraw > balance:
            print("Insufficient balance")
        else:
            balance = balance - withdraw
            print("Your balance is:", balance)

    case 4:
        print("Thank you for using ATM")

    case _:
        print("Invalid choice")