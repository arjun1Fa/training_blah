'''Display seats, book a seat, cancel a booking, check whether a seat is already booked'''

seat_num_list = []


def book_seat():
    num = int(input("Enter the number of seats you want to book: "))
    count = 1

    while count <= num:
        seat_number = int(input("Please enter seat number " + str(count) + ": "))

        if seat_number in seat_num_list:
            print("This seat is already occupied. Please choose another.")
        else:
            seat_num_list.append(seat_number)
            print("Seat", seat_number, "booked successfully.")
            count += 1


def displaySeats():
    if len(seat_num_list) == 0:
        print("No seats are booked.")
    else:
        print("Booked seats are:", seat_num_list)


def checkSeat():
    seat_number = int(input("Enter seat number to check: "))

    if seat_number in seat_num_list:
        print("Seat", seat_number, "is already booked.")
    else:
        print("Seat", seat_number, "is available.")


def cancelBooking():
    seat_number = int(input("Enter seat number to cancel: "))

    if seat_number in seat_num_list:
        seat_num_list.remove(seat_number)
        print("Booking cancelled successfully.")
    else:
        print("Seat is not booked.")


def main():
    choice = 0

    while choice != 5:

        print("\n------ MENU ------")
        print("1. Book Seat")
        print("2. Check Seat")
        print("3. Display Seats")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_seat()

        elif choice == 2:
            checkSeat()

        elif choice == 3:
            displaySeats()

        elif choice == 4:4
            cancelBooking()

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()