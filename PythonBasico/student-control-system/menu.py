import actions, data
from tkinter import Tk, filedialog
import csv

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
            print("\n==== Ingresar estudiante ====")
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
            print("\n==== Ver promedio de notas por estudiante ====")
            student_name = actions.request_student_name()
            actions.get_student_avg(student_name)
            
        case 5:
            print("\n==== Eliminar estudiante ====")
            student_name = actions.request_student_name()
            actions.delete_student(student_name)
        case 6:
            print("\n==== Ver estudiantes reprobados ====")
            actions.get_reproved_students()
        case 7:
            print("\n==== Exportar datos a csv ====")
        case 8: 
            print("\n==== Importar datos de csv ====")
            data.import_student_csv()

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