num = int(input("Enter number to reverse "))
reverse = 0

while num !=0:

    digit = num%10
    reverse = reverse*10 +digit
    num//= 10

print(reverse , "is the number")