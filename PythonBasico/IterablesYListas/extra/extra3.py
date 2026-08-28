my_list = [9, 4, 7, 1, 5]
min_value= my_list[0]
for num in my_list:
    if num < min_value:
        min_value = num

print(f"El menor valor es {min_value}")