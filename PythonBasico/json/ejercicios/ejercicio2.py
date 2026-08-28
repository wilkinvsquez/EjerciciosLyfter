import json

FILE_PATH = "./Pokemon.json"
NEW_FILE_PATH = "./New_Pokemon.json"

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def write_json_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def request_pokemon_info():
    print("----- Información General ------")
    name = input("Inserte el nombre del nuevo pokemon: ")
    type = input("Inserte el tipo del pokemon: ")
    level = int(input("Inserte el nivel del pokemon: "))
    weight_kg = float(input("Inserte el peso en kg del pokemon: "))
    is_shiny = input("¿Es shiny? (True/False): ").lower() == "true"
    held_item = input("Inserte el objeto que porta el pokemon: ")

    print("----- Habilidades ------")
    skill_1 = input("Inserte la primera habilidad: ")
    skill_2 = input("Inserte la segunda habilidad: ")
    skill_3 = input("Inserte la tercera habilidad: ")
    skill_4 = input("Inserte la cuarta habilidad: ")

    print("----- Stats ------")
    hp = int(input("Inserte los HP: "))
    attack = int(input("Inserte el ataque: "))
    defense = int(input("Inserte la defensa: "))
    sp_attack = int(input("Inserte el ataque especial: "))
    sp_defense = int(input("Inserte la defensa especial: "))
    speed = int(input("Inserte la velocidad: "))

    new_pokemon = {
            "name": name,
            "type": type,
            "level": level,
            "weight_kg": weight_kg,
            "is_shiny": is_shiny,
            "held_item": held_item,
            "skills": [skill_1, skill_2, skill_3, skill_4],
            "stats": {
                "hp": hp,
                "attack": attack,
                "defense": defense,
                "sp_attack": sp_attack,
                "sp_defense": sp_defense,
                "speed": speed
            }
        }
    return new_pokemon

def main():
    pokemon_list = read_file(FILE_PATH)
    new_pokemon = request_pokemon_info()
    pokemon_list.append(new_pokemon)
    write_json_file(NEW_FILE_PATH,json.dumps(pokemon_list))

main()