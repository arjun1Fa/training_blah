numbers =[]
even =[]
odd = []
for i in range(8):
    num = int(input("Enter the number "))
    numbers.append(num)

for num in numbers:
    if num%2==0:
        even.insert(0,num)
    else :
        odd.insert(0,num)

print("The original list" , numbers,"\n")
print("Even numebrs " , even,"\n")
print("odd numbers" , odd,"\n")
