# print_numbers_times_2\
# Esta funcion es O(n) tanto en el mejor caso como en el peor caso
def print_numbers_times_2(numbers_list):    # O(n)
	for number in numbers_list:             # O(n)
		print(number * 2)                   # O(1)


# check_if_lists_have_an_equal
# El mejor caso es O(1) y el peor de los casos es O(n^2)
def check_if_lists_have_an_equal(list_a, list_b):   # O(n^2)
	for element_a in list_a:                        # O(1)
		for element_b in list_b:                    # O(n^2)
			if element_a == element_b:              # O(1)
				return True                         # O(1)
				
	return False                                    # O(1)

# print_10_or_less_elements
# Esta funcion es O(1) tanto en el mejor caso como en el peor caso
def print_10_or_less_elements(list_to_print):       
	list_len = len(list_to_print)                   # O(1)  
	for index in range(min(list_len, 10)):          # O(1)
		print(list_to_print[index])                 # O(1)

# generate_list_trios
# Esta funcion es O(n^3) tanto en el mejor caso como en el peor caso
def generate_list_trios(list_a, list_b, list_c):
	result_list = []                                                        # O(1)
	for element_a in list_a:                                                # O(1)
		for element_b in list_b:                                            # O(n^2)
			for element_c in list_c:                                        # O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')  # O(1)
				
	return result_list                                                      # O(1)