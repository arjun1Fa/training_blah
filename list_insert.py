'''input 15  numbers and create a list where all numebrs greaste than 50 are inerted in the beginning o a nnew list '''

numbers =[]

for i in range(15):
    num = int(input("Enter the number "))
    numbers.append(num)
    
new_list =[]
for num in numbers:
    if num > 50:
        new_list.insert(0,num)

print("Original List ", numbers, "\n")
print("New list = ", new_list , "\n")

