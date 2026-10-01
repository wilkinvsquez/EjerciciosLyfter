from datetime import datetime
def log_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        args_str = ", ".join(str(a) for a in args)
        print(f"func:{func.__name__} - args: {args_str} - [{datetime.now()}] - Resultado: {result}")
        return result

    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for param in (*args, *kwargs.values()):
            if not isinstance(param, (int, float)):
                raise ValueError("Los valores deben ser numericos")
        return func(*args, **kwargs)
    return wrapper

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

print("Resultado", multiply(3, 4))
