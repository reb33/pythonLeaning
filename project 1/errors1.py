try:
    print ("Hi men")
    print (1/0)
except ZeroDivisionError:
    print ("caught ZeroDivisionError")
except NameError:
    print("caught NameError")
except:
    print("caught all others errors")
finally:
    print("It's my finally")

try:
    print ("Second Try")
    #name not defined
    print (name+1)
except (ZeroDivisionError, NameError):
    print ("caught ZeroDivisionError or NameError")
except:
    print("caught all others errors")
finally:
    print("It's my finally")

try:
    print ("Third Try")
    #For cath SyntaxError need insert code to eval
    eval("print('Hi third try')d")
except (ZeroDivisionError, NameError, SyntaxError):
    print ("caught ZeroDivisionError or NameError or SyntaxError")
except:
    print("caught all others errors")
finally:
    print("It's my finally")

print ("End of the program")