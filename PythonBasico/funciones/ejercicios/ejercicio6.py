def separate_and_sort (text_to_sort):
    words_list = text_to_sort.split('-')
    words_list.sort()
    return '-'.join(words_list)


print(separate_and_sort("arca-computadora-funcion-perro-monitor-python-variable"))