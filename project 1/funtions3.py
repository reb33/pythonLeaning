def printStr(name):
    print ("Hi " +name()+"!")

def getName():
    return "::"+input("Введите имя: ")+"::"

printStr(getName)