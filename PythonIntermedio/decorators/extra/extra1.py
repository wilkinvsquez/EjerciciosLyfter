def repeat_twice(func):
    def wrapper(*args):
        func(*args)
        return func(*args)
    return wrapper

@repeat_twice
def great(name):
    print(f"Hola {name}")

great("Wilkin")