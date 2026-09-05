print("--------- RAILWAY TICKET SYSTEM ---------")

print("1. Book Ticket")
print("2. Cancel Ticket")
print("3. check fare")
print("4. check seat availability")

choice=int(input("Enter your choice: "))

match choice:
    
    case 1:
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        from_place = input("Enter starting station: ")
        to_place = input("Enter destination: ")

        print("\nTicket Booked Successfully!")
        print("Name:", name)
        print("Age:", age)
        print("From:", from_place)
        print("To:", to_place)

    case 2:
        ticket_no = int(input("Enter ticket number: "))

        print("Ticket", ticket_no, "cancelled successfully.")

    case 3:
        distance = float(input("Enter distance in KM: "))

        fare = distance * 2

        print("Total Fare: ₹", fare)

    case 4:
        seat_no = int(input("Enter seat number: "))

        print("Seat", seat_no, "is available.")

    case _:
        print("Invalid choice!")