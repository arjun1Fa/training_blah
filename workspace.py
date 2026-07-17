num_list = []

# Input 10 numbers
for i in range(10):
    num = int(input("Enter number " + str(i + 1) + ": "))
    num_list.append(num)

# Delete negative numbers using del
for i in range(len(num_list) - 1, -1, -1):
    if num_list[i] < 0:
        print(num_list[i], "was deleted")
        del num_list[i]

# Pop the last 3 numbers (if available)
for i in range(min(3, len(num_list))):
    print("Popped:", num_list.pop())

print("Current list:", num_list)

# Clear the list if it has more than 5 elements
if len(num_list) > 5:
    num_list.clear()

print("Final list:", num_list)