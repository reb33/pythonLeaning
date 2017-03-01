cond1 = "ааа";
cond2 = "ббб";
cond3 = "ввв";

print("Начало")
if cond1 == "ааа":
    print("cond1_1")
    print("cond1_2")
    print(cond1)
    if cond2 == "ббб":
        print("cond2_1")
        print(cond2)
    print("cond1_3")
    print(cond1)
    if cond2 == "бб":
        print("cond2_2")
        print(cond2)
    if cond3 == "вв":
        print("cond3_1")
        print(cond3)
    else:
        print("cond3_2")
        print(cond3)
    if cond1 == "вв":
        print("cond1_3")
        print(cond1)
print("Конец")


x=0
if x<0:
    sign=-1
    print("Negative")
elif x==0:
    sign=0
    print("Zero")
else:
    sign=1
    print("Positive")
print(sign)