def aplanaTask(mass):
    mass1 = sorted(mass[:int(len(mass)/2)], reverse=True)
    if len(mass) % 2 != 0:
        mass1.append(mass[int(len(mass)/2)])
    mass1 +=sorted(mass[len(mass)-int(len(mass)/2):], reverse=True)

    ret = []
    for x in zip(mass, mass1):
        ret.append(x[0] - x[1])

    print(ret)


aplanaTask([1,2,3,4,5,6,7])