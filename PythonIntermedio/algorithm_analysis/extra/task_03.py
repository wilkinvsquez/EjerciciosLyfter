def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

# ¿Cuál es la complejidad temporal?
    # R/
    #   - Al existir en el metodo 2 ciclos anidados se convierte en una complejidad de O(n^2)
# ¿Cuanto dura si hay 1 millón de claves?
    # R/
    #   - con 1 millon de claves el print se ejecuta 1 millon X 1 millon = 1 billon de veces, lo cuial podria tardar dias incluso si cada print fuera muy rapido
    