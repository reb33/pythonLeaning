#Кортежи нельзя изменять, но увеоичивают производительность
tupleExam1 = "one", "two", "three"
tupleExam2 = (1,2,3,(1,2,3))

print(tupleExam1[1])
print(tupleExam2[3])

try:
    tupleExam1[0] = 2
except TypeError:
    print("Кортежи не изменяются")
    # raise