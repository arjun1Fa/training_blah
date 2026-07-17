choice =0
num_list =[]
num =0
while choice != 3:
    print("Enter your choice : \n 1 for insertion at the beginning \n 2 for deletion from the beginning \n 3 for displaying the list \n 4 for exiting the program")
    choice = int(input())

    if choice==1:
        num = int(input("Enter the numebr you want to input"))
        num_list.append(num)
    
    elif choice==2:
        print(num_list.pop(0))
    elif choice ==3:
        break
    elif choice ==4:
        print(num_list )
    else:
        print("Invalid input")