number_list = []
repeated_number_count = 0
list_length = int(input("Please enter the length of the list: "))

for i in range(list_length):
    number = int(input(f"Please enter number {i + 1}: "))
    number_list.append(number)

search_number = int(input("Please enter number to see how many times is on the list: "))
for number in number_list:
    if number ==search_number:
        repeated_number_count += 1

print (f"El numero {search_number} aparece {repeated_number_count} {"veces" if repeated_number_count>1 else "vez"}" )