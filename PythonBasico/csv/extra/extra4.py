import csv

file_path = "./VideoGameList.csv"

def read_csv(file_path):
    with open(file_path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def find_information(file_content, developer):
    results = []
    for row in file_content[1:]:
        if developer.upper() in row[2].upper():
            results.append(row)
    return results

def request_developer():
    return input("Inserte la desarrollador a buscar: ")

def show_ordered_info(matched_information, developer):
    print(f"Videojuegos desarrollados por {developer}")
    for item in matched_information:
        print(f" - {item[0]} (Clasificación: {item[3]}, Género: {item[1]})")

def main():
    user_selection = request_developer()
    file_information =  read_csv(file_path)
    results = find_information(file_information, user_selection)
    show_ordered_info(results, user_selection)


main()