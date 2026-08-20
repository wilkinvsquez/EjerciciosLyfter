import json

FILE_PATH = "./Pokemon.json"
NEW_FILE_PATH = "./Pokemon.json"
NEW_POKEMON= {
		"name": "Charmander_test",
		"type": "Fire",
		"level": 8,
		"weight_kg": 8.5,
		"is_shiny": True,
		"held_item": "Charcoal",
		"skills": ["Ember", "Scratch", "Tackle", "Smokescreen"],
		"stats": {
			"hp": 39,
			"attack": 52,
			"defense": 43,
			"sp_attack": 60,
			"sp_defense": 50,
			"speed": 65
		}
	}

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def write_json_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def main():
    pokemon_list = read_file(FILE_PATH)
    pokemon_list.append(NEW_POKEMON)
    write_json_file(NEW_FILE_PATH,json.dumps(pokemon_list))

main()