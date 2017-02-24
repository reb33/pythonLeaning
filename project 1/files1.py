file = open("resources/text1.txt", "w")
file.write("very long text")
file.close()

del file

file = open("resources/text1.txt", "a")
file.write("\nSecond line")
file.close()

with open("resources/text1.txt", "r") as f:
    print(f.read())
#автоматическое закрытие после with