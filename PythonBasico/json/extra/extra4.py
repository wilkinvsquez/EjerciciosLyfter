import json

FILE_PATH = "./Pokemon.json"

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()
        json_converted = json.loads(text_content)
        return json_converted

def group_by_type(pokemon_list):
    return sorted(pokemon_list, key=lambda x:x["type"])
    
def get_type_list(sorted_pokemon_list):
    types_list = []
    for pokemon in sorted_pokemon_list:
        if not pokemon["type"] in types_list:
            types_list.append(pokemon["type"])

    return types_list

def get_average_by_type(sorted_pokemon_list):
    average_dict = {}
    types_list = get_type_list(sorted_pokemon_list)
    
    for type in types_list:
        test_list = list(filter(lambda x:x["type"]==type, sorted_pokemon_list))
        sum_values = 0
        for item in test_list:
            sum_values += item["level"]
        average_dict[type] = sum_values / len(test_list)
    return average_dict

def show_pokemon_info(average_by_type):
    for key, value in average_by_type.items():
        print(f"Tipo: {key} -> Promedio de nivel: {value}")
        
def main():
    pokemon_list = read_file(FILE_PATH)
    grouped_list = group_by_type(pokemon_list)
    average_by_type = get_average_by_type(grouped_list)
    show_pokemon_info(average_by_type)

main()