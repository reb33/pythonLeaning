import functools


class Logger:
    def __init__(self, func):
        self.func = func
        self.log = []

    def __call__(self, *args, **kwargs):
        functools.wraps(self.func)
        self.log.append((args, kwargs))
        return self.func(*args, **kwargs)


@Logger
def summ_all(*args, **kwargs):
    '''Сумировать все'''
    mass = []
    for x in args:
        mass.append(x)
    for key, value in kwargs.items():
        mass.append((key,value))
    return mass

# summ_all = Logger(summ_all)


print(summ_all(1,2,3, y=5))
print(summ_all.log)

print(summ_all.__name__)
print(summ_all.__doc__)