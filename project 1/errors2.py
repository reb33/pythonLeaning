try:
    a = 1
    if (a==1):
        raise ValueError("a equals 1")
except ValueError:
    print("next raise got error")
    raise