import csv, os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def import_student_csv():
    """Opens a file picker dialog and returns the selected file's path."""
    Tk().withdraw()
    path = askopenfilename(
        title="Seleccione el archivo CSV a importar",
        filetypes=[("CSV files", "*.csv")]
    )
    return path