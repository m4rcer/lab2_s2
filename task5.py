import re

text = input("Введите текст: ")

pattern = r"(\b[A-Z][a-z]*\d{2}(\d{2})?\b)"

matches = re.finditer(pattern, text)

for match in matches:
    print(match[1])
