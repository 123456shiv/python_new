print("----- ATM WITHDRAW SYSTEM -----")

balance = float(input("Enter your account balance: ₹"))
withdraw = float(input("Enter withdrawal amount: ₹"))

match True:

    case _ if withdraw <= 0:
        print("Invalid withdrawal amount.")

    case _ if withdraw > balance:
        print("Insufficient Balance.")
        print("Your Balance: ₹", balance)

    case _ if withdraw % 100 != 0:
        print("Please enter amount in multiples of ₹100.")

    case _:
        balance = balance - withdraw

        print("\n----- TRANSACTION SUCCESSFUL -----")
        print("Withdrawn Amount: ₹", withdraw)
        print("Remaining Balance: ₹", balance)