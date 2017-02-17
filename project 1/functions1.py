def factorial(number):
    ret = 1;
    for el in range(1,number+1):
        ret *= el
    return ret

print (factorial(5))