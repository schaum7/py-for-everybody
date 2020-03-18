import re
import os

path_ipsum_file = os.path.join(os.path.dirname(__file__), "text.txt")

with open(path_ipsum_file, "r", encoding="UTF-8") as file:
    for line in file:
        line = line.strip()
        print(line)
        words = re.findall("\S+", line)
        print(words)
        print(len(words))
