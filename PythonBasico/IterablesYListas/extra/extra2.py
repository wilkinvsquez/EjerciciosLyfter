my_list = [3, 6, 0, -2, 4]
is_negative_or_0 = False

#Esta es una manera de hacerlo pero supuse que no es lo que se quiere con el ejercicio
#is_negative_or_0 = any(num <= 0 for num in my_list)

print(my_list)

for num in my_list:
    if num <= 0:
        is_negative_or_0 = True 

print(f"{"Hay al menos un numero negativo o 0" if is_negative_or_0 else "Todos los numeros son positivos"}")