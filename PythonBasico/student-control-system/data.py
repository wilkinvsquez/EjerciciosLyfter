from tkinter import Tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import json, csv

STUDENT_PATH = './students.json'
MIN_GRADE = 60
SUBJECT_LABELS = {
    "spanish": "Español",
    "english": "Inglés",
    "history": "Estudios Sociales",
    "science": "Ciencias",
}

def import_student_csv():
    """Opens a file picker dialog and returns the selected file's path."""
    Tk().withdraw()
    path = askopenfilename(
        title="Seleccione el archivo CSV a importar",
        filetypes=[("CSV files", "*.csv")]
    )
    return path

def request_export_path():
    """Opens a save dialog and returns the chosen file path."""
    Tk().withdraw()
    path = asksaveasfilename(
        title="Guardar como",
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")]
    )
    return path

def export_students(students_list, fieldnames, file_path):
    """Writes the given students to a CSV file at file_path."""
    with open(file_path, "w", encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_list)

def build_student_from_row(row):
    """Converts a raw CSV row (all strings) into a proper student dict."""
    student = {
        "name": row["name"],
        "section": row["section"],
    }
    for key in SUBJECT_LABELS.keys():
        student[key] = float(row[key])
    return student

def get_students():
    """Returns the list of saved students, or an empty list if none exist yet."""
    try:
        return read_json_file(STUDENT_PATH)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students_list):
    """Overwrites the students file with the given list."""
    create_json_file(STUDENT_PATH, json.dumps(students_list, ensure_ascii=False, indent=2))

def read_json_file(file_path):
    """Reads and parses a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
        return json.loads(text_content)

def read_csv_file(file_path):
    """Reads a CSV file and returns a list of row dictionaries."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def create_json_file(path, content):
    """Writes text content to a file, overwriting it if it already exists."""
    with open(path, "w", encoding='utf-8') as file:
        file.write(content)