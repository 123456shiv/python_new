print("\n----- CHARACTER TYPE MENU -----")
print("1. Vowel")
print("2. Consonant")
print("3. Digit")
print("4. Special Character")

choice = input("Enter your choice(1-4): ")

match choice:
    case "1":
        ch = input("Enter a character: ")
        if ch in "aeiouAEIOU":
            print("You entered a vowel.")
        else:
            print("Invalid input.")

    case "2":
        ch = input("Enter a character: ")
        if ch.isalpha() and ch not in "aeiouAEIOU":
            print("You entered a consonant.")
        else:
            print("Invalid input.")

    case "3":
        ch = input("Enter a number: ")
        if ch.isdigit():
            print("You entered a digit.")
        else:
            print("Invalid input.")

    case "4":
        ch = input("Enter a special character: ")
        if not ch.isalnum():
            print("You entered a special character.")
        else:
            print("Invalid input.")

    case _:
        print("Invalid choice.")