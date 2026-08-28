import json

FILE_PATH = "./Pokemon.json"

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def request_user_search():
    return input("Ingrese el tipo de pokemon desea buscar(electric, fire, water, grass, normal, ghost, fighting): ")

def search_pokemon(pokemon_list,user_search):
    pokemon_matches = []
    for pokemon in pokemon_list:
        if pokemon["type"].lower() == user_search.lower():
            pokemon_matches.append(pokemon)

    return pokemon_matches

def show_matches(pokemon_matches):
    if len(pokemon_matches) == 0:
        print("No hay registros de pokemones de este tipo")
        return
    print("Los pokemones que existen de ese tipo son: ")
    for pokemon in pokemon_matches:
        print(f"- {pokemon["name"]}")

def main():
    pokemon_list = read_file(FILE_PATH)
    user_search= request_user_search()
    matches = search_pokemon(pokemon_list, user_search)
    show_matches(matches)


main()