base_number = 1
user_number = int(input("Ingrese un número entero: "))
total_sum = 0

while base_number <= user_number:
    total_sum += base_number
    base_number += 1

print(f"{user_number} -> {total_sum}")