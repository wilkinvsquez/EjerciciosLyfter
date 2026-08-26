import csv

file_path = "./VideoGameList.csv"

def read_csv(file_path):
    with open(file_path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def count_by_gender(videogames_list):
    genders_count = {}
    for item in videogames_list[1:]:
        gender = item[1]
        if gender in genders_count:
            genders_count[gender] += 1
        else:
            genders_count[gender] = 1
    return genders_count
    

def show_ordered_info(genders_count):
    print("Géneros encontrados:")
    for gender in sorted(genders_count):
        print(f"{gender}: {genders_count[gender]}")

def main():
    file_content = read_csv(file_path)
    genders_count = count_by_gender(file_content)
    show_ordered_info(genders_count)


main()