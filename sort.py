a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")


x = [a, b, c]
for i in range(len(x)):
    for j in range(i + 1, len(x)):
        if x[i] > x[j]:
            x[i], x[j] = x[j], x[i]

print("The numbers in ascending order are:", x)