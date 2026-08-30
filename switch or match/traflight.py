colour=input("Enter the colour of the traffic light (red, yellow, green): ").strip().lower()

match colour:
    case "red":
        print("Stop")

    case "yellow":
        print("Get ready to move")

    case "green":
        print("Go")

    case _:
        print("Invalid colour input. Please enter red, yellow, or green.")