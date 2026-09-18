balance=int(input("Enter your account balance: "))
withdrawal_amount=int(input("Enter the amount you want to withdraw: "))

if withdrawal_amount <= 0:
    print("Invalid withdrawal amount. Please enter a positive value.")

elif withdrawal_amount % 100 != 0:
    print("Amount must be a multiple of 100")

elif withdrawal_amount > balance:
    print("Insufficient balance")

elif balance - withdrawal_amount < 500:
    print("Minimum balance of 500 must be maintained")

else:
    balance = balance - withdrawal_amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)