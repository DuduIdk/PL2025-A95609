import re

file = open("TPC2\obras.csv", "r", encoding="utf-8")

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
        line += " " + newLine
        reg = re.split(r';(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
        
    compositor = f"{reg[4]}"
    compositores.append(compositor)        
    periodo = f"{reg[3]}"
    numObrasPeriodo[periodo] = numObrasPeriodo.get(periodo, 0) + 1
    titulo = f"{reg[0]}"
    obrasPeriodo[periodo] = obrasPeriodo.get(periodo, []) + [titulo]
    
    
compositores.sort()
for periodo in obrasPeriodo:
    obrasPeriodo[periodo].sort()
    
print(compositores)
print(numObrasPorPeriodo)
print(obrasPeriodo)


