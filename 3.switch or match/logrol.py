print("____Login role system____")
print("1. Admin")
print("2. User")
print("3. Student")
print("4. Guest")

choice=int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("\n ----login succesfull --")
        print("Welcome Admin")
        print("You have full access to the system.")

    case 2:
        print("\n ----login succesfull --")
        print("Welcome User")
        print("You have limited access to the system.")

    case 3:
        print("\n ----login succesfull --")
        print("Welcome Student")
        print("You have access to student resources.")

    case 4:
        print("\n ----login succesfull --")
        print("Welcome Guest")
        print("You have limited access to the system.")

    case _:
        print("\nInvalid choice. Please select a valid option (1-4).")