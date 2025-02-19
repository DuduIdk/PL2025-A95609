import re

file = open("./obras.csv", "r", encoding="utf-8")

ignoreHeader = file.readline()

compositores =[]

while line:
    print(line.strip())
    line = file.readline()
    reg = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    while len(reg) < 7:
        newLine = file.readLine().strip()
        if not newLine:
            break



