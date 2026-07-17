n = int(input("Enter the number of words: "))

words = []

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

groups = {}

for word in words:
    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

print("\nAnagram Groups:")
for group in groups.values():
    print(group)