word = input("Enter the word:")
i = 0
count = 0

while i < len(word):
    if word[i] in "aeiouAEIOU":
        count += 1
    i += 1

print(count)
