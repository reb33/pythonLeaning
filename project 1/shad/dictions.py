dict1 = {"alice": 1, "polly": 3, "agata": 5, "freeda": 2, "liza": 6, "alexandra": 1, "alice":8}
del dict1["alice"]
print(dict1)

for key, value in dict1.items():
    print(value, key)

print(any((k, v) == ("polly", 3)
          for k, v in dict1.items()))

print("\nSORTED")
for key, value in sorted(dict1.items()):
    print(value, key)
