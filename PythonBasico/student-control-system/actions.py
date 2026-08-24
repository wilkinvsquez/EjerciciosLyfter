import re, json

# Option 1: Ingresar estudiante
STUDENT_PATH = './students.json'

def request_non_empty_text(message):
    while True:
        value = input(message).strip()
        print(value)
        if value and all(caracter.isalpha() or caracter.isspace() for caracter in value):
            return value
        print("Este campo solo puede contener letras.")

def request_for_number(message, min_value, max_value):
    while True:
        try:
            value = float(input(f"{message} ({min_value}-{max_value}): "))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"El valor debe estar entre {min_value} y {max_value}.")
        except ValueError:
            print("Debe ingresar un número válido.")

def request_section():
    while True:
        section = input("Ingrese el grupo al que pertenece ('11B'): ").strip().upper()
        if re.fullmatch(r"\d{1,2}[A-Z]", section):
            return section
        print("Formato inválido. Debe ser 2 números seguidos de una letra, ej: 11B")

def student_exists(name, students_list):
    return any(student["name"] == name for student in students_list)

def request_student_info():
    name = request_non_empty_text("Ingrese el el nombre completo del estudiante: ")
    section = request_section()
    spanish_sub = request_for_number("Digite la nota de Español: ",0,100)
    english_sub = request_for_number("Digite la nota de Inglés: ",0,100)
    history_sub = request_for_number("Digite la nota de Estudios Sociales: ",0,100)
    science_sub = request_for_number("Digite la nota de Ciencias: ",0,100)

    student = {
        "name" : name,
        "section" : section,
            "grades" : {
                "spanish" : spanish_sub,
                "english" : english_sub,
                "history" : history_sub,
                "science" : science_sub,
            }
    }
    return student

def save_student():
    students_list = []
    try:
        students_list = list(read_file(STUDENT_PATH))
    except FileNotFoundError:
        print("[info] => No existen registro de estudiantes")
    student = request_student_info()
    if student_exists(student["name"], students_list):
        print("El estudiante ya se encuentra registrado.")
        return False
    else:
        students_list.append(student)
        create_file(STUDENT_PATH, json.dumps(students_list))
        return True

# Option 2: Ver todos los estudiantes
def get_students_list():
    try:
        students_list = list(read_file(STUDENT_PATH))
        for index, student in enumerate(students_list) : 
            print(f"{index + 1}. {student["name"]} -> Seccion {student["section"]}")

    except FileNotFoundError:
        print("[info] => No existen registro de estudiantes")

# Option 3: Ver top 3 con mejor nota
def calc_grade_average(grades):
    average = 0
    for grade in grades.values():
        average += grade
    return average / len(grades)

def get_grades_averages():
    student_list_averages = []
    student_list = list(read_file(STUDENT_PATH))
    for student in student_list:
        average= calc_grade_average(student["grades"])
        student_list_averages.append({student["name"]:average})
    return student_list_averages

def get_top_three_average(student_averages):
    print("Quede aqui")

#General
def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def create_file(path, content):
    with open(path, "w", encoding='utf-8') as file:
        file.write(content)




