import re

filename = input("Введите имя текстового файла: ")

with open(filename, "r") as f:
    text = f.read()

pattern = r"(int|short|byte)\s+([a-zA-Z_]\w*)\s*=\s*(-?\d+)\s"

matches = re.findall(pattern, text)

for match in matches:
    print("Найдено совпадение: {0} {1} = {2}".format(match[0], match[1], match[2]))