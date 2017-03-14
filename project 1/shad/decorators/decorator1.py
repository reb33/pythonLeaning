import functools


def notify_call(func):
    #для созранения имени функции и документации
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        print("Called "+func.__name__)
        return func(*args, **kwargs)
    return decorated


@notify_call
def summ(a, b):
    '''Сумирование'''
    return a + b

# g = notify_call(summ)
# x = g(2, 3)
# print(str(x))

print(str(summ(2, 5)))

print(summ.__name__)
print(summ.__doc__)
