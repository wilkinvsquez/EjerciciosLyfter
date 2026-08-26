# 1. Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
#   Ejemplo:
#       Entrada:
#           "programacion"
#           "Ingrese el carácter que desea buscar:" "o"
#       Salida:
#           "Se ha encontrado 2 veces el carácter"

def find_letter(text, letter):
    count = text.count(letter)
    return count

text =  input("Ingrese el texto a evaluar: ")
letter =  input("Ingrese el carácter que desea buscar:")
print(f"Se han encontrado {find_letter(text, letter)} el caracter")