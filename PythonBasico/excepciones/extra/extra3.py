def total_values(value_list):
    total = 0
    for value in value_list:
        try:
            converted_value = (float(value))
            total+=converted_value
            print(f"{value} sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {value}")
    print(f"Total de la suma: {total}")



my_list = ['10', 'manzana', '5.5', '3', 'n/a']
total_values(my_list)