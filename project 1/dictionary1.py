dict = {
    "один":1,
    2:"два",
    3:{
        "3_1":"подтип1",
        "3_2":"подтип2"
    }
}

print (dict["один"])
print(dict[3]["3_1"])

try:
    print(dict[4])
except KeyError:
    print("Такого ключа нет")

print(dict.get(4))

if 4 in dict:
    print("Ключ есть")
else:
    print("Ключа нет")