
def main():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número")

    age = input("Ingrese su edad: ")
    if not age.isdigit():
        raise ValueError("Numero invalido")
    
    print(f"Hola {name}, su edad es {age}")


main()