num_list = []

for i in range(10):
    num = int(input("Enter number " +str(i+1)+ " into the list "))
    num_list.append(num)

for i in range(len(num_list) -1,-1 ,-1 ):
    if num_list[i]<0:
        print(num_list[i], " was deleted")
        del num_list[i]

print(num_list.pop())
print(num_list.pop())
print(num_list.pop())

print("The current list is " ,num_list)

if len(num_list) >5:
    num_list.clear()






    


