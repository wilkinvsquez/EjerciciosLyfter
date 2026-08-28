my_list = [4, 3, 6, 1, 7]
# -1 indica el último elemento de la lista, -2 el penúltimo, etc.
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)


#temporal = my_list[0]
#my_list[0] = my_list[len(my_list)-1]
#my_list[len(my_list)-1] = temporal
#print(my_list)