def logger(func):
    def wrapper(*args):
        print("Params: ", args)
        res = func(*args)
        print("Return: ", res)
        return res
    return wrapper

@logger
def sumar(a,b):
    return a + b

sumar(2, 3)