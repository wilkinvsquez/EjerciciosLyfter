# 01: BUBBLE_SORT

def bubble_sort(number_list):
    indent_1 = "    "                                                                               # O(1)
    indent_2 = "        "                                                                           # O(1)
    for outer_index in range(0, len(number_list) - 1):                                              # O(n^2)
        changes_made = False                                                                        # O(1)
        print(f"-- Iteracion {outer_index} --")                                                     # O(1)
        for index in  range(0, len(number_list) -1 - outer_index ):                                 # O(n^3)
            print(f"{indent_1}-- Sub iteracion {index} --")                                         # O(1)

            current_value = number_list[index]                                                      # O(1)
            next_value = number_list[index + 1]                                                     # O(1)

            print(f"{indent_2}Current Value: {current_value}")                                      # O(1)
            print(f"{indent_2}Next Value: {next_value}")                                            # O(1)

            if current_value > next_value:                                                          # O(1)
                print(f"{indent_2}El elemento actual es mayor al siguiente. Intercambiandolos...")  # O(1)
                number_list[index] = next_value                                                     # O(1)
                number_list[index + 1] = current_value                                              # O(1)
                changes_made = True                                                                 # O(1)

            print(f"{indent_2}Number List updated: {number_list}")                                  # O(1)
        if not changes_made:                                                                        # O(1)
            print("\nNo hubo cambios, la lista ya está ordenada.")                                  # O(1)
        return                                                                                      # O(1)

    print(f"\n{indent_1}Resultado {outer_index}: {number_list}")                                    # O(1)
print("-" * 60)                                                                                     # O(1)

test_list = [18, -11, 68, 6, 32, 53, -2]                                                            # O(1)
bubble_sort(test_list)                                                                              # O(n^2)