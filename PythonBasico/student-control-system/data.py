from tkinter import Tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
import csv

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

def read_csv_file(file_path):
    """Reads a CSV file and returns a list of row dictionaries."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)