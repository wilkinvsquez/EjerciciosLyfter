count = 1
number = int(input("Ingrese un número del 1 al 10: "))

while number < 1 or number > 10:
    number = int(input("Ese número no es válido. Ingrese un número del 1 al 10: "))

while count <= 12:
    print(f"{number} x {count} = {number * count}")
    count += 1