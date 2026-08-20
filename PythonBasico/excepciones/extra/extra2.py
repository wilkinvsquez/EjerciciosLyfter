def parse_to_int(strings_list):
    print("Resultado:")
    for index in range(len(strings_list)):
        try:
            aux = strings_list[index]
            strings_list[index] = int( strings_list[index])
            print(f"'{aux}' convertido a {strings_list[index]}")
        except ValueError as e:
            print(f"No se pudo convertir el elemento: {strings_list[index]}")

my_list = ['4', 'hola', '10', '5.2']
parse_to_int(my_list)