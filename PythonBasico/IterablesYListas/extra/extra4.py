def calculateAverage (values):
    quantity_value = len(values)
    total = 0
    for value in values:
        total += value
    average = total / quantity_value
    return average


my_list = [10, 20, 30, 40, 50]
new_list = []
average = calculateAverage(my_list)
for value in my_list:
    if average < value:
        new_list.append(value)



print(f"""
    Promedio: {average}
    Nueva lista: {new_list}
""")
