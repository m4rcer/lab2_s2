with open('task1.txt', 'r', encoding="utf8") as f:
    text = f.read()

text = text.lower()

letter_count = {}
for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

for char in sorted(letter_count, letter_count.get, True):
    print(char, letter_count[char])