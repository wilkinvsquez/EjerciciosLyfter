def addition(num_list):
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise TypeError("[Error]: Existen valores no numericos")
    return sum(num_list)

def average(num_list):
    if not num_list:
        raise ValueError("La lista no puede estar vacia")
    for num in num_list:
        if not isinstance(num, (int, float)):
            raise TypeError("[Error]: Existen valores no numericos")
    return sum(num_list) / len(num_list)

def celsius_a_fahrenheit(value):
    if not isinstance(value, (int, float)):
        raise TypeError("[Error]: El valor a convertir no es numerico")
    return value * 9 / 5 + 32