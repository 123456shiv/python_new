print("===== MINI BANKING APPLICATION =====")

balance = 0
account_created = False
account_number = 0
name = ""
pin = ""

while True:

    print("\n1. Create Account")
    print("2. Check Balance")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer Money")
    print("6. Change PIN")
    print("7. Account Details")
    print("8. Exit")

    choice = int(input("\nEnter your choice: "))

    match choice:

        case 1:
            if account_created:
                print("Account already exists!")

            else:
                name = input("Enter your name: ")
                account_number = int(input("Enter account number: "))
                pin = input("Set your 4-digit PIN: ")

                balance = float(input("Enter initial deposit: "))

                account_created = True

                print("\nAccount created successfully!")
                print("Account Holder:", name)
                print("Account Number:", account_number)
                print("Balance: ₹", balance)

        case 2:
            if account_created:
                print("Current Balance: ₹", balance)
            else:
                print("Please create an account first.")

        case 3:
            if account_created:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance = balance + amount
                    print("Amount deposited successfully!")
                    print("Updated Balance: ₹", balance)
                else:
                    print("Invalid amount!")

            else:
                print("Please create an account first.")

        case 4:
            if account_created:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount!")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance = balance - amount
                    print("Amount withdrawn successfully!")
                    print("Remaining Balance: ₹", balance)

            else:
                print("Please create an account first.")

        case 5:
            if account_created:
                receiver = int(input("Enter receiver account number: "))
                amount = float(input("Enter transfer amount: "))

                if amount <= 0:
                    print("Invalid amount!")

                elif amount > balance:
                    print("Insufficient balance!")

                elif receiver == account_number:
                    print("Cannot transfer money to your own account!")

                else:
                    balance = balance - amount

                    print("₹", amount, "transferred successfully!")
                    print("Receiver Account:", receiver)
                    print("Remaining Balance: ₹", balance)

            else:
                print("Please create an account first.")

        case 6:
            if account_created:
                old_pin = input("Enter old PIN: ")

                if old_pin == pin:
                    new_pin = input("Enter new PIN: ")

                    if len(new_pin) == 4:
                        pin = new_pin
                        print("PIN changed successfully!")
                    else:
                        print("PIN must contain 4 digits!")

                else:
                    print("Incorrect old PIN!")

            else:
                print("Please create an account first.")

        case 7:
            if account_created:
                print("\n===== ACCOUNT DETAILS =====")
                print("Account Holder:", name)
                print("Account Number:", account_number)
                print("Balance: ₹", balance)

            else:
                print("Please create an account first.")

        case 8:
            print("Thank you for using Mini Banking Application!")
            break

        case _:
            print("Invalid choice! Please enter 1-8.")