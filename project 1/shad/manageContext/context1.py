class Context:
    def __init__(self, stop_exceptions, returnData):
        print("__init__")
        self.stop_exceptions = stop_exceptions
        self.returnData = returnData

    def __enter__(self):
        print("__enter__")
        return self.returnData

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__({}, {}, {})".format(exc_type, exc_val, exc_tb))
        return self.stop_exceptions


with Context(True, "Mark") as c:
    print("Hi "+c)
    raise RuntimeError("Smth wrong")
