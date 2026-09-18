menu=input("Enter the menu item: ").strip().lower()

match menu:
    case "pizza":
        print("You have selected Pizza.")

    case "pasta":
        print("You have selected Pasta.")

    case "salad":
        print("You have selected Salad.")


    case "tea":
        print("You have selected Tea.")

    case _:
        print("Invalid menu item. Please select from Pizza, Pasta, or Salad.")
