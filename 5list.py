n1 =[]
n2 =[]
n3 =[]
n4 =[]
n5 =[]
n6 =[]


for i in range(3):
    num = int(input("Enter the number "))
    n1.append(num)
    
n6.extend(n1)
for i in range(3):
    num = int(input("Enter the number "))
    n2.append(num)
    
for i in range(3):
    num = int(input("Enter the number "))
    n3.append(num)
    
for i in range(3):
    num = int(input("Enter the number "))
    n4.append(num)
    
for i in range(3):
    num = int(input("Enter the number "))
    n5.append(num)
    
n1.extend(n2)
n1.extend(n3)
n1.extend(n4)
n1.extend(n5)

print("The first list is ",n6, "\n")
print("The second list is ",n2, "\n")
print("The third list is ",n3 ,"\n")
print("The first list is ",n4 ,"\n")
print("The first list is ",n5 ,"\n")

print("The joined list is ",n1 ,"\n")




