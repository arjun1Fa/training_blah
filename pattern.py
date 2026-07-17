rows = int(input("Enter the number of rows for the pyramid\t"))

for i in range(rows , 0 ,-1):
    print("\t" ," " * (rows - i) + "*" * (2 * i - 1))
