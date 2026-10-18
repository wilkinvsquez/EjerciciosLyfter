# 01: BUBBLE_SORT WITH VALIDATIONS

def bubble_sort(number_list):
    validate_bubble_sort(number_list)
    iteration_counter = 0
    changes_counter = 0
    print(f"Lista Inicial: {number_list}")
    
    for outer_index in range(0, len(number_list) - 1):
        changes_made = False
        iteration_counter += 1
        for index in  range(0, len(number_list) -1 - outer_index ):
            current_value = number_list[index]
            next_value = number_list[index + 1]

            if current_value > next_value:
                changes_counter += 1
                number_list[index] = next_value
                number_list[index + 1] = current_value
                changes_made = True

        if not changes_made:
            break

    print(f"Lista Ordenada: {number_list}")
    print(f"Iteraciones: {iteration_counter}")
    print(f"Intercambios: {changes_counter}")
    print("-" * 60)

def validate_bubble_sort(values_list):
    if not values_list:
        raise ValueError("La lista se encuentra vacia")
    if not all(isinstance(x,(int)) for x in values_list):
        raise TypeError("Error: La lista contiene elementos no numéricos")
    

test_list = [18, -11, 68, None, 32, 53, -2]
test_list2 = [5,4,3,2,1]
test_list3 = [5, "Hola", 2]
test_list_empty = []

bubble_sort(test_list_empty)