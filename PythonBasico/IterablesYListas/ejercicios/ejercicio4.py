my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair_list = []

for index in my_list:
    if index % 2 != 0:
        continue
    pair_list.append(index)
print(pair_list)