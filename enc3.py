text = input("Enter the string: ")

result = ""
i = 0

while i < len(text):
    letter = text[i]
    i += 1

    number = ""

    while i < len(text) and text[i].isdigit():
        number += text[i]
        i += 1

    result += letter * int(number)

print(result)