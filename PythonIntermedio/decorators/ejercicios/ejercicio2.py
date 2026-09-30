def are_params_number(func):
    def wrapper(*args):
        for param in args:
            if not isinstance(param,(int, float)):
                raise ValueError("Los parametros no son valores numericos")
        return func(*args)
    return wrapper

@are_params_number
def sumar(a, b):
    return a + b

print(sumar(2, 3))
print(sumar(2, "3"))    