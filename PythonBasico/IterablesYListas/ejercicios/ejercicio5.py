count = 0
list_numbers = []
highest_number = 0

while count < 10:
    user_number = int(input("Ingrese un número: "))
    list_numbers.append(user_number)
    if user_number > highest_number:
        highest_number = user_number
    count += 1

print(f"{list_numbers}. El mas alto fue: {highest_number}.")