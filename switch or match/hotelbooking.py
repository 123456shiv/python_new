print("----- HOTEL BILLING SYSTEM -----")

room_charge = 0
food_charge = 0

print("\n----- HOTEL MENU -----")
print("1. Room Booking")
print("2. Food Order")
print("3. Check Bill")
print("4. Checkout")

choice = int(input("Enter your choice (1-4): "))

match choice:

    case 1:
        print("\n----- ROOM TYPES -----")
        print("1. Single Room  - ₹1000/day")
        print("2. Double Room  - ₹1800/day")
        print("3. Deluxe Room  - ₹2500/day")

        room = int(input("Enter room type (1-3): "))
        days = int(input("Enter number of days: "))

        match room:
            case 1:
                room_charge = 1000 * days
                print("Single Room booked successfully.")

            case 2:
                room_charge = 1800 * days
                print("Double Room booked successfully.")

            case 3:
                room_charge = 2500 * days
                print("Deluxe Room booked successfully.")

            case _:
                print("Invalid room choice.")

        print("Room Charge: ₹", room_charge)

    case 2:
        print("\n----- FOOD MENU -----")
        print("1. Breakfast  - ₹150")
        print("2. Lunch      - ₹250")
        print("3. Dinner     - ₹300")
        print("4. Coffee     - ₹100")

        food = int(input("Enter food choice (1-4): "))
        quantity = int(input("Enter quantity: "))

        match food:
            case 1:
                food_charge = 150 * quantity
                print("Breakfast ordered successfully.")

            case 2:
                food_charge = 250 * quantity
                print("Lunch ordered successfully.")

            case 3:
                food_charge = 300 * quantity
                print("Dinner ordered successfully.")

            case 4:
                food_charge = 100 * quantity
                print("Coffee ordered successfully.")

            case _:
                print("Invalid food choice.")

        print("Food Charge: ₹", food_charge)

    case 3:
        total_bill = room_charge + food_charge

        print("\n----- HOTEL BILL -----")
        print("Room Charge: ₹", room_charge)
        print("Food Charge: ₹", food_charge)
        print("----------------------")
        print("Total Bill: ₹", total_bill)

    case 4:
        print("\nThank you for staying with us!")
        print("Have a nice day.")

    case _:
        print("\nInvalid choice.")