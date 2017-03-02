print("ZIP")
mass1 = [1,3,5]
mass2 = [3,8,9]
for x in zip(mass1,mass2):
    print (x)

print()
print("ENUMERATE")
for x in enumerate(mass2):
    print(x)

print()
print("SORTED")
mass3 = [3,6,22,6,2,3,9,10,1]
print(sorted(mass3))
print(sorted(mass3, reverse=True))
mass3.sort()
print(mass3)
mass3.sort(reverse=True)
print(mass3)

def get_second(x):
    return x[1]

mass4=[("a",3,"b"),("c",5,"c"),("b",3,"a"),("d",4,"f"),("f",6,"b")]
print(sorted(mass4, key=lambda x:[x[1],x[2]]))
print(sorted(mass4, key=get_second, reverse=True))
