choice = int(input("Enter the shape you want to calculate: "))

match choice:
    case 1:
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("The area of the circle is:", area)

    case 2:
        side = float(input("Enter the side length of the square: "))
        area = side * side
        print("The area of the square is:", area)

    case 3:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("The area of the rectangle is:", area)

    case 4:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("The area of the triangle is:", area)

    case _:
        print("Invalid choice. Please enter a valid choice between 1 and 4.")   