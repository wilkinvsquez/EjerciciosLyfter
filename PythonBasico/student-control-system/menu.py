import actions

def start():
    while True:
        menu= get_menu("main")
        try:
            user_selection = int(input(menu))
        except ValueError:
            print("[Error] => Debe ingresar un numero valido, Intente de nuevo")

        if user_selection < 1 or user_selection > 9:
            print("[Error] => Opcion inválida, intente de nuevo")
            continue

        handle_selection(user_selection)

        return user_selection

def handle_selection(option_selected):
    match option_selected:
        case 1:
            print("==== Ingresar estudiante ====")
            if actions.save_student():
                print("Se ha registrado el estudiante exitosamente.")
            else:
                print("[Error] => ")
        case 2:
            print("2. Ver informacion de estudiante")
        case 3:
            print("3. Ver top 3 con mejor nota")
        case 4:
            print("4. Ver promedio de notas por estudiante")
        case 5:
            print("5. Eliminar estudiante")
        case 6:
            print("6. Ver estudiantes reprobados")
        case 7:
            print("7. Exportar datos a csv")
        case 8:
            print("8. Importar datos de csv")





def get_menus():
    return {
        "main": """
==== Sistema de Control de Estudiantes ====

1. Ingresar estudiante
2. Ver informacion de estudiante
3. Ver top 3 con mejor nota
4. Ver promedio de notas por estudiante
5. Eliminar estudiante
6. Ver estudiantes reprobados
7. Exportar datos a csv
8. Importar datos de csv
9. Salir

Seleccione una opcion: """
    }

def get_menu(menu_name):
    menus= get_menus()
    return menus[menu_name]