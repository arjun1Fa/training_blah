'''input a3b2c4 , output aaabbcccc'''

text = input("Enter the string: ")

result = ""

for i in range(0, len(text), 2):
    letter = text[i]
    count = int(text[i + 1])
    result += letter * count

print(result)


