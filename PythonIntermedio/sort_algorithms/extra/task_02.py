# 01: BUBBLE_SORT WITH ITERATIONS AND CHANGES

def bubble_sort(number_list):
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

test_list = [18, -11, 68, 6, 32, 53, -2]
test_list2 = [5,4,3,2,1]
bubble_sort(test_list2)