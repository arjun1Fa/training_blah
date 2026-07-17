num_list = []

for i in range(10):
    num = int(input("Enter number " +str(i+1)+ " into the list "))
    num_list.append(num)

print(num_list)

mid =  int(len(num_list)/2)
end =  len(num_list)
for i in range(mid):
    del num_list[0]
print("Deleted")

for i in range (mid , end):
    print(num_list.pop())

print(num_list)
