while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program exited.")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Sum =", a + b)
    elif choice == 2:
        print("Difference =", a - b)
    elif choice == 3:
        print("Product =", a * b)
    elif choice == 4:
        if b != 0:
            print("Quotient =", a / b)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice.")