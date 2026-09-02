print("----- PIZZA MENU -----")
print("1. Margherita  199")
print("2. farmhouse  249")
print("3. Veggie paradise  299")
print("4. panner pizza  349")
print("5. Cheese corn pizza  399")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        print("You have selected Margherita pizza.")
        print("Price: 199")
    case 2:
        print("You have selected farmhouse pizza.")
        print("Price: 249")
    case 3:
        print("You have selected Veggie paradise pizza.")
        print("Price: 299")
    case 4:
        print("You have selected panner pizza.")
        print("Price: 349")
    case 5:
        print("You have selected Cheese corn pizza.")
        print("Price: 399")
    case _:
        print("Invalid choice.")
    