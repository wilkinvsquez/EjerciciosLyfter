import actions

def start():
    while True:
        menu= get_menu("main")
        try:
            user_selection = int(input(menu))
            if user_selection < 1 or user_selection > 9:
                print("\n[Error] => Opcion inválida, intente de nuevo")
                continue

            if user_selection == 9:
                        print("Gracias por su visita, Vuelva pronto!!")
                        break
            
            handle_selection(user_selection)
        except ValueError:
            print("\n[Error] => Debe ingresar un numero valido, Intente de nuevo")



        #return user_selection

def handle_selection(option_selected):
    match option_selected:
        case 1:
            print("==== Ingresar estudiante ====")
            if actions.save_student():
                print("\nSe ha registrado el estudiante exitosamente.")
            else:
                print("[Error] => ")
        case 2:
            print("\n==== Lista de estudiantes ====")
            actions.get_students_list()
        case 3:
            print("\n==== Top 3 Promedios ====")
            actions.get_top_three_average()
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
2. Ver informacion de todos los estudiantes
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