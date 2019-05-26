import zwierzeta
filePath = r"zwierzeta.txt"

with open(filePath) as file:
    linesList = file.read().splitlines()
file.close()

linesList = linesList[1:]
al = zwierzeta.Zwierzeta(linesList)

for a in al.animalList:
    print(a)
