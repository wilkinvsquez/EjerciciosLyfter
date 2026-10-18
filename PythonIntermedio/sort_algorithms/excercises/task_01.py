# 01: BUBBLE_SORT

def bubble_sort(number_list):
    indent_1 = "    "
    indent_2 = "        "
    for outer_index in range(0, len(number_list) - 1):
        changes_made = False
        print(f"-- Iteracion {outer_index} --")
        for index in  range(0, len(number_list) -1 - outer_index ):
            print(f"{indent_1}-- Sub iteracion {index} --")

            current_value = number_list[index]
            next_value = number_list[index + 1]

            print(f"{indent_2}Current Value: {current_value}")
            print(f"{indent_2}Next Value: {next_value}")

            if current_value > next_value:
                print(f"{indent_2}El elemento actual es mayor al siguiente. Intercambiandolos...")
                number_list[index] = next_value
                number_list[index + 1] = current_value
                changes_made = True

            print(f"{indent_2}Number List updated: {number_list}")
        if not changes_made:
            print("\nNo hubo cambios, la lista ya está ordenada.")
            return

        print(f"\n{indent_1}Resultado {outer_index}: {number_list}")
        print("-" * 60)

test_list = [18, -11, 68, 6, 32, 53, -2]
bubble_sort(test_list)