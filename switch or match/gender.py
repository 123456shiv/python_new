gender=input("Enter your gender (male/female): ").split()[0].lower()

match gender:
    case "male":
        print("You are a male.")

    case "female":
        print("You are a female.")

    case _:
        print("Invalid input. Please enter 'male' or 'female'.")

    