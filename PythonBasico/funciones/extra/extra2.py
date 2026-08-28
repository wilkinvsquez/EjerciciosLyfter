# 2. Cree una función que reciba una lista de palabras y un número n, y 
#    retorne una nueva lista con solo las palabras que tengan más de n letras
#   Ejemplo:
#       Entrada:
#           ["cielo", "sol", "maravilloso", "día"]
#           "Ingrese el numero de letras minimas en la palabra: " 4'
#       Salida:
#           ["cielo", "maravilloso"]
def find_words_bigger_than_n(list, number):
    aux_list=[]
    for word in list:
        if len(word) >= number:
            aux_list.append(word)
    return aux_list

word_quantity = int(input("Cuantas palabras te gustaria evaluar: "))
words=[]
counter = 1
while counter<=word_quantity:
    word = input(f"Inserte su palabra numero {counter}: ")
    words.append(word)
    counter += 1

number_of_letters = int(input("Ingrese el numero de letras minimas en la palabra: "))
print(find_words_bigger_than_n(words, number_of_letters))


