import re, json

# Option 1: Ingresar estudiante
STUDENT_PATH = './students.json'
MIN_GRADE = 60

def request_non_empty_text(message):
    """Keeps asking until the user enters non-empty, letters-only text."""

    while True:
        value = input(message).strip()
        if value and all(caracter.isalpha() or caracter.isspace() for caracter in value):
            return value
        print("Este campo solo puede contener letras.")

def request_for_number(message, min_value, max_value):
    """Keeps asking until the user enters a number within the given range."""

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
    """Keeps asking until the user enters a valid section format (e.g. '11B')."""

    while True:
        section = input("Ingrese el grupo al que pertenece ('11B'): ").strip().upper()
        if re.fullmatch(r"\d{1,2}[A-Z]", section):
            return section
        print("Formato inválido. Debe ser 2 números seguidos de una letra, ej: 11B")

def student_exists(name, students_list):
    """Checks whether a student with the given name is already in the list."""
    return any(student["name"] == name for student in students_list)  

def request_student_name():
    student_name = request_non_empty_text("Ingrese el el nombre del estudiante: ")
    return student_name


def request_student_info():
    """Collects and returns a full student record (name, section, and grades)."""

    name = request_non_empty_text("Ingrese el nombre completo del estudiante: ")
    section = request_section()

    subjects = {
        "spanish": "Español",
        "english": "Inglés",
        "history": "Estudios Sociales",
        "science": "Ciencias",
    }

    grades = {}
    for key, label in subjects.items():
        grades[key] = request_for_number(f"Digite la nota de {label}: ", 0, 100)

    student = {
        "name": name,
        "section": section,
        "grades": grades,
    }
    return student

def save_student():
    """Registers a new student, unless one with the same name already exists.
    Returns:
        bool: True if the student was saved, False if it already existed."""

    students_list = get_students()
    student = request_student_info()
    if student_exists(student["name"], students_list):
        print("El estudiante ya se encuentra registrado.")
        return False
    else:
        students_list.append(student)
        save_students(students_list)
        return True

# Option 2: Ver todos los estudiantes
def get_students_list():
        """Prints every saved student with their section."""

        students_list = get_students()
        if not students_list:
            print("[info] => No existen registro de estudiantes")
            return
        print_numbered_list(students_list, lambda student: f"{student['name']} -> Seccion {student['section']}")


# Option 3: Ver top 3 con mejor nota
def calc_grade_average(grades):
    """Returns the average of a student's grades."""
    return sum(grades.values()) / len(grades)

def get_grades_averages():
    """Returns a list of {name, average} for every saved student."""

    student_list_averages = []
    for student in get_students():
        average= calc_grade_average(student["grades"])
        student_list_averages.append({"name" : student["name"], "average" : average})
    return student_list_averages

def get_top_three_average():
    """Prints the top 3 students with the highest grade average."""

    averages= get_grades_averages()
    sorted_list = sorted(averages, key=lambda student: student["average"], reverse=True)[:3]
    print_numbered_list(sorted_list, lambda student: f"{student['name']} => {student['average']}")

# Option 4: Ver promedio de notas por estudiante
def get_student_avg(student_name):
    """Prints a specific student's grade average, or a not-found message."""

    students = get_students()
    matching_students = [student for student in students if student["name"] == student_name]
    if not matching_students:
        print(f"No se encontró ningún estudiante con el nombre '{student_name}'.")
        return

    student = matching_students[0]
    average = calc_grade_average(student["grades"])
    print(f"{student['name']} => {average}")
    
# Option 5: Eliminar estudiante
def delete_student(student_name):
    """Removes a student by name, or prints a not-found message."""

    student_list = get_students()
    matching_students = [student for student in student_list if student["name"] == student_name]
    if not matching_students:
        print(f"No se encontró ningún estudiante con el nombre '{student_name}'.")
        return
    student_list_updated = [student for student in student_list if student["name"] != student_name]

    save_students(student_list_updated)
    print(f"Se eliminó al estudiante '{student_name}' exitosamente.")

def get_reproved_students():
    """Returns a list of reproved students"""

    students_averages = get_grades_averages()
    reproved = [student for student in students_averages if student["average"] < MIN_GRADE]
    print_numbered_list(reproved, lambda student: f"{student['name']} -> {student['average']}")


#General
def read_file(file_path):
    """Reads and parses a JSON file."""

    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
        return json.loads(text_content)

def create_file(path, content):
    """Writes text content to a file, overwriting it if it already exists."""

    with open(path, "w", encoding='utf-8') as file:
        file.write(content)

def get_students():
    """Returns the list of saved students, or an empty list if none exist yet."""

    try:
        return read_file(STUDENT_PATH)
    except FileNotFoundError:
        return []

def save_students(students_list):
    """Overwrites the students file with the given list."""

    create_file(STUDENT_PATH, json.dumps(students_list, ensure_ascii=False, indent=2))

def print_numbered_list(items, format_line):
    """Prints each item as a numbered line, using format_line(item) as the text."""
    
    for index, item in enumerate(items):
        print(f"{index + 1}. {format_line(item)}")

