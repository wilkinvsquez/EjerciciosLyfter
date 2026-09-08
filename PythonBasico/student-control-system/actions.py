import re, data

# Option 1: Ingresar estudiante
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

def student_exists(name, section, students_list):
    """Checks whether a student with the given name and section already exists."""
    return any(student["name"] == name and student["section"] == section for student in students_list) 

def request_student_name():
    student_name = request_non_empty_text("Ingrese el nombre del estudiante: ")
    return student_name


def request_student_info():
    """Collects and returns a full student record (name, section, and grades)."""
    name = request_non_empty_text("Ingrese el nombre completo del estudiante: ")
    section = request_section()

    student = {
        "name": name,
        "section": section,
    }
    for key, label in data.SUBJECT_LABELS.items():
        student[key] = request_for_number(f"Digite la nota de {label}: ", 0, 100)

    return student


def save_student():
    """Registers a new student, unless one with the same name already exists.

    Returns:
        bool: True if the student was saved, False if it already existed.
    """
    students_list = data.get_students()
    if not students_list:
        print("[info] => No existen registro de estudiantes, se creara uno nuevo")
    student = request_student_info()
    if student_exists(student["name"], student["section"], students_list):
        print("El estudiante ya se encuentra registrado.")
        return False
    else:
        students_list.append(student)
        data.save_students(students_list)
        return True

# Option 2: Ver todos los estudiantes
def get_students_list():
        """Prints every saved student with their section."""

        students_list = data.get_students()
        if not students_list:
            print("[info] => No existen registro de estudiantes")
            return
        print_numbered_list(students_list, lambda student: f"{student['name']} -> Seccion {student['section']}")


# Option 3: Ver top 3 con mejor nota
def calc_grade_average(student):
    """Returns the average of a student's grades."""
    grades = [student[key] for key in data.SUBJECT_LABELS.keys()]
    return sum(grades) / len(grades)

def get_grades_averages():
    """Returns a list of {name, average} for every saved student."""

    student_list_averages = []
    for student in data.get_students():
        average = calc_grade_average(student)
        student_list_averages.append({"name" : student["name"], "average" : average})
    return student_list_averages

def get_top_three_average():
    """Prints the top 3 students with the highest grade average."""

    averages= get_grades_averages()
    sorted_list = sorted(averages, key = lambda student: student["average"], reverse = True)[:3]
    print_numbered_list(sorted_list, lambda student: f"{student['name']} => {student['average']}")

# Option 4: Ver promedio de notas por estudiante
def get_student_avg(student_name):
    """Prints a specific student's grade average, or a not-found message."""

    students = data.get_students()
    matching_students = [student for student in students if student["name"] == student_name]
    if not matching_students:
        print(f"No se encontró ningún estudiante con el nombre '{student_name}'. \nIntenta colocando el nombre completo del estudiante.")
        return

    student = matching_students[0]
    average = calc_grade_average(student)
    print(f"{student['name']} => {average}")
    
# Option 5: Eliminar estudiante
def delete_student(student_name, student_section):
    """Removes a student by name and section, after confirming with the user."""
    student_list = data.get_students()
    if not student_exists(student_name, student_section, student_list):
        print(f"No se encontró ningún estudiante '{student_name}' en la sección '{student_section}'.")
        return

    if not request_confirmation(f"¿Confirma que desea eliminar a '{student_name}' de la sección '{student_section}'?"):
        print("Operación cancelada.")
        return

    updated_list = [s for s in student_list if not (s["name"] == student_name and s["section"] == student_section)]
    data.save_students(updated_list)
    print(f"Se eliminó al estudiante '{student_name}' exitosamente.")

def request_confirmation(message):
    """Keeps asking until the user answers yes or no. Returns True for yes."""
    while True:
        answer = input(f"{message} (s/n): ").strip().lower()
        if answer in ("s", "si"):
            return True
        if answer in ("n", "no"):
            return False
        print("Respuesta inválida. Escriba 's' o 'n'.")

# Option 6: Ver estudiantes reprobados
def get_reproved_students():
    """Prints every student with at least one failing grade, along with the failed subjects."""
    students_list = data.get_students()
    if not students_list:
        print("[info] => No existen registro de estudiantes")
        return

    reproved = []
    for student in students_list:
        failed_subjects = get_failed_subjects(student)
        if failed_subjects:
            reproved.append({"name": student["name"], "section": student["section"], "failed": failed_subjects})

    if not reproved:
        print("[info] => No hay estudiantes reprobados")
        return

    print_numbered_list(reproved, lambda s: f"{s['name']} - Sección {s['section']} -> " + ", ".join(f"{label}: {grade}" for label, grade in s['failed']))

def get_failed_subjects(student):
    """Returns a list of (label, grade) tuples for subjects where the student scored below MIN_GRADE."""
    return [(label, student[key])
            for key, label in data.SUBJECT_LABELS.items()
            if student[key] < data.MIN_GRADE
    ]

# Option 7: Exportar datos a csv
def export_CSV_student_list():
    """Exports all saved students to a CSV file chosen by the user."""
    student_list = data.get_students()
    if not student_list:
        print("[info] => No hay estudiantes para exportar")
        return

    file_path = data.request_export_path()
    fieldnames = ["name", "section"] + list(data.SUBJECT_LABELS.keys())

    data.export_students(student_list, fieldnames, file_path)
    print(f"Estudiantes exportados exitosamente a '{file_path}'")

# Option 8: Importar datos de csv
def import_student_list():
    """Merges the students from a CSV file into the saved students, skipping duplicates."""
    file_path = data.import_student_csv()
    if not file_path:
        print("[info] => No se seleccionó ningún archivo para importar.")
        return

    try:
        importation_rows = data.read_csv_file(file_path)
    except FileNotFoundError:
        print(f"[Error] => No se encontró el archivo '{file_path}'.")
        return

    current_students = data.get_students()
    importation_students = [data.build_student_from_row(row) for row in importation_rows]

    for student in importation_students:
        if student_exists(student["name"], student["section"], current_students):
            print(f"'{student['name']}' ya se encuentra registrado, se omite.")
        else:
            current_students.append(student)

    data.save_students(current_students)
    print("Students imported succesfully")

#General
def print_numbered_list(items, format_line):
    """Prints each item as a numbered line, using format_line(item) as the text."""
    for index, item in enumerate(items):
        print(f"{index + 1}. {format_line(item)}")

