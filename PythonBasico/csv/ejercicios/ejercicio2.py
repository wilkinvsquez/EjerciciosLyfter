import csv

def request_info():
    game_count = int(input("Digite la cantidad de videojuegos que deseas agregar: "))
    game_dict_list = []
    counter = 1
    while counter <= game_count:
        print(f"--------- Videojuego #{counter} ---------")
        name = input("Ingrese el nombre del videojuego: ")
        gender = input("Ingrese el genero del videojuego: ")
        developer = input("Ingrese el desarrollador del videojuego: ")
        clasification = input("Ingrese la clasificacion del videojuego: ")

        videogame = {
            "Nombre": name,
            "Genero": gender,
            "Desarrollador": developer,
            "Clasificacion": clasification
        }

        game_dict_list.append(videogame)
        counter +=1
    return game_dict_list

def create_csv(file_path, game_list):
    with open(file_path, "w", newline='') as file:
        headers = game_list[0].keys()
        writer= csv.DictWriter(file, fieldnames = headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(game_list)

def main():
    game_list = request_info()
    create_csv('./VideoGameListTabs.csv', game_list)

main()

