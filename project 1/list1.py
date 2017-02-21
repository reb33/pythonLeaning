listExem = [1 , 23, 43, 5, 3, 5, 3, "2", "wre", [2, 3, 4, 5]]

listExem += ["Hi", "All"]
listExem.append(['Everybody'])

print(listExem)

if ['Everybody'] in listExem:
    print(True)

print(listExem.count(5))
print(len(listExem))
print(listExem[1])
print(listExem[9][1])