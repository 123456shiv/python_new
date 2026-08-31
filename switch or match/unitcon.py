choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        km = float(input("Enter value in kilometer: "))
        meter = km * 1000
        print(km, "km =", meter, "meter")

    case 2:
        meter = float(input("Enter value in meter: "))
        centimeter = meter * 100
        print(meter, "m =", centimeter, "cm")

    case 3:
        kg = float(input("Enter value in kilogram: "))
        gram = kg * 1000
        print(kg, "kg =", gram, "gram")

    case 4:
        liter = float(input("Enter value in liter: "))
        milliliter = liter * 1000
        print(liter, "L =", milliliter, "ml")

    case _:
        print("Invalid choice")