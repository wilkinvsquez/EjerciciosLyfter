# 3. Cree una función que reciba un string y retorne cuántas vocales contiene
#   Ejemplo:
#       Entrada:
#           "Hola mundo"
#       Salida:
#           4

def vocal_count(text): 
    vocals = "aeiou"
    count = 0
    for letter in text:
        if letter in vocals:
            count += 1
    return count

print(vocal_count("Hola Mundo"))