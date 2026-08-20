import json

FILE_PATH = "./Pokemon.json"

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def show_pokemon_info(pokemon_list):
    for index, pokemon in enumerate(pokemon_list):
        print(f"""
----- Pokemon #{index+1}
Nombre: {pokemon["name"]}
Tipo:   {pokemon["type"]}
Nivel:  {pokemon["level"]}
""")

def main():
    pokemon_list = read_file(FILE_PATH)
    show_pokemon_info(pokemon_list)

main()