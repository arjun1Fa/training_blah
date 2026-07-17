student = [
    ["arjun", "pathummi", "aachi", "ameen"],
    [1, 10, 0, 1],
    [1333, 324252, 2, 5]
]

total = 0
for i in range(1, len(student)):
    total += student[i][0]

print("Student Name:", student[0][0])
print("Total Marks:", total)