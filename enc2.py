text =input("Enter a string")
result = ""
for ch in text:
    result += chr(ord(ch) + 1)

print(result)