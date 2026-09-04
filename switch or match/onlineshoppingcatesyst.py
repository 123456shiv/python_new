print("----- ONLINE SHOPPING CATEGORY -----")

print("1. Electronics")
print("2. Clothing")
print("3. Grocery")
print("4. Footwear")
print("5. Books")

choice = int(input("Enter your category (1-5): "))

match choice:

    case 1:
        print("\n----- ELECTRONICS -----")
        print("1. Mobile")
        print("2. Laptop")
        print("3. Headphones")

        item = int(input("Enter your item choice (1-3): "))

        match item:
            case 1:
                print("You selected Mobile.")
            case 2:
                print("You selected Laptop.")
            case 3:
                print("You selected Headphones.")
            case _:
                print("Invalid item choice.")

    case 2:
        print("\n----- CLOTHING -----")
        print("1. T-Shirt")
        print("2. Jeans")
        print("3. Jacket")

        item = int(input("Enter your item choice (1-3): "))

        match item:
            case 1:
                print("You selected T-Shirt.")
            case 2:
                print("You selected Jeans.")
            case 3:
                print("You selected Jacket.")
            case _:
                print("Invalid item choice.")

    case 3:
        print("\n----- GROCERY -----")
        print("1. Rice")
        print("2. Milk")
        print("3. Bread")

        item = int(input("Enter your item choice (1-3): "))

        match item:
            case 1:
                print("You selected Rice.")
            case 2:
                print("You selected Milk.")
            case 3:
                print("You selected Bread.")
            case _:
                print("Invalid item choice.")

    case 4:
        print("\n----- FOOTWEAR -----")
        print("1. Sports Shoes")
        print("2. Sandals")
        print("3. Slippers")

        item = int(input("Enter your item choice (1-3): "))

        match item:
            case 1:
                print("You selected Sports Shoes.")
            case 2:
                print("You selected Sandals.")
            case 3:
                print("You selected Slippers.")
            case _:
                print("Invalid item choice.")

    case 5:
        print("\n----- BOOKS -----")
        print("1. Python Book")
        print("2. Data Science Book")
        print("3. Novel")

        item = int(input("Enter your item choice (1-3): "))

        match item:
            case 1:
                print("You selected Python Book.")
            case 2:
                print("You selected Data Science Book.")
            case 3:
                print("You selected Novel.")
            case _:
                print("Invalid item choice.")

    case _:
        print("\nInvalid category.")