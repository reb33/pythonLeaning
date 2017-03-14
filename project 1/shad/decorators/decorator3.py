import functools


def check_ret_type(type_):
    def decorator(func):
        functools.wraps(func)

        def decorated(*args, **kwargs):
            val = func(*args, **kwargs)
            assert isinstance(val, type_), "return value %r does not match %s" % (val,type_)
            return val
        return decorated
    return decorator

# def returns(rtype):
#     def check_returns(f):
#         def new_f(*args, **kwds):
#             result = f(*args, **kwds)
#             assert isinstance(result, rtype), \
#                    "return value %r does not match %s" % (result,rtype)
#             return result
#         # new_f.func_name = f.func_name
#         return new_f
#     return check_returns

# @check_ret_type(float)
@check_ret_type(str)
def division(a, b):
    return a / b

print(division(1, 2))