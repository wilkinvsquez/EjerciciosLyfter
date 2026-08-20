def get_and_validate_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    return name

def get_and_validate_age():
    try:
        age = int(input("Ingrese su edad: "))
        return age
    except ValueError:
        print("Número no valido")


def main():
    name = get_and_validate_name()
    age = get_and_validate_age()
    
    print(f"Hola {name}, su edad es {age}")


main()