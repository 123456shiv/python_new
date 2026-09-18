print("----- GAME CHARACTER SELECTION -----")

print("1. Warrior")
print("2. Archer")
print("3. Mage")
print("4. Assassin")

choice = int(input("Enter your character choice (1-4): "))

match choice:

    case 1:
        print("\n----- CHARACTER SELECTED -----")
        print("Character: Warrior")
        print("Weapon: Sword")
        print("Power: High Attack")
        print("Speed: Medium")

    case 2:
        print("\n----- CHARACTER SELECTED -----")
        print("Character: Archer")
        print("Weapon: Bow")
        print("Power: Medium Attack")
        print("Speed: High")

    case 3:
        print("\n----- CHARACTER SELECTED -----")
        print("Character: Mage")
        print("Weapon: Magic Staff")
        print("Power: High Magic")
        print("Speed: Low")

    case 4:
        print("\n----- CHARACTER SELECTED -----")
        print("Character: Assassin")
        print("Weapon: Dagger")
        print("Power: High Critical Attack")
        print("Speed: Very High")

    case _:
        print("\nInvalid character choice.")