import csv

file_path = "./VideoGameList.csv"

def read_csv(file_path):
    with open(file_path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def find_information(file_content, classification):
    results = []
    for row in file_content[1:]:
        if classification.upper() in row[3]:
            results.append(row)
    return results

def request_classification():
    return input("Inserte la clasificación ESRB a buscar: ")

def show_ordered_info(matched_information):
    for item in matched_information:
        print("-----------------------")
        print(f"Nombre: {item[0]}")
        print(f"Género: {item[1]}")
        print(f"Desarrollador: {item[2]}")
        print(f"Clasificación: {item[3]}")

def main():
    user_selection =request_classification()
    file_information =  read_csv(file_path)
    results = find_information(file_information, user_selection)
    show_ordered_info(results)


main()