name = "Alex"
age = 21

print("Я %s, мне %d лет" % (name, age))
print()
print("Я {}, мне {} лет".format(name, age))
print()
print("Я {1}, мне {0} лет".format(name, age))
print()

# Alex****** <
# ******Alex >
# ***Alex*** ^

length = str(len(name)+6)
print(("Я {:*^"+length+"}, мне {} лет").format(name,age))