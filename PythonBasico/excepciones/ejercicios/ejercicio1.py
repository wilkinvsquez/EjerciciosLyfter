def show_menu(total):
    while True:
        menu = f"""
Total number: {total}
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar Resultado
6. Salir

Elija una opcion: """
        try:
            option_selected = int(input(menu))
            
        except ValueError:
            print("[Error] => Debe ingresar un numero valido, Intente de nuevo")
            continue

        if option_selected < 1 or option_selected > 6:
            print("[Error] => Opcion inválida, intente de nuevo")
            continue

        return option_selected

            
def calculate_operation(total, option_selected):
    try:
        number = int(input("Ingrese el numero: "))
    except ValueError:
        print("Error: debe ingresar un número válido")
        return total

    match option_selected:
        case 1:
            total = total + number
        case 2:
            total = total - number
        case 3:
            total = total * number
        case 4:
            try:
                total = total / number
            except ZeroDivisionError:
                print("[Error]: El numero no se puede dividir entre 0")

    return total

def main():
    total = 0
    while True:
        option_selected = show_menu(total)

        if option_selected == 5:
            total = 0
            print("El total se ha reestablecido!")
            continue

        if option_selected == 6:
            print("Gracias por su visita, Vuelva pronto!!")
            break

        total = calculate_operation(total, option_selected)

if __name__ == '__main__':
    main()