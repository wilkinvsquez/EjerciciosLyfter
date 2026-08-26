import csv

file_path = "./VideoGameList.csv"

def read_csv(file_path):
    with open(file_path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def show_information(file_content):
    for item in file_content[1:]:
        print("-----------------------")
        print(f"Nombre: {item[0]}")
        print(f"Género: {item[1]}")
        print(f"Desarrollador: {item[2]}")
        print(f"Clasificación: {item[3]}")

def main():
    content = read_csv(file_path)
    show_information(content)

main()