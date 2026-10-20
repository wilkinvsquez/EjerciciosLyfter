def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


#¿Cuál es la complejidad de cada algoritmo?
    # R/
    #   - En linear_search en el peor de los casos va a recorrer la lista completa buscando el objetivo con el riesgo de que este de ultimo o incluso no se encuentre en la lista. Si hay 1000 valores en la lista, podria recorrerlo 1000 veces por lo que la complejidad seria O(n)
    #   - binary_search en cada vuelta del while realiza una comparacion con el objetivo, y descarta la mitad de la lista que puede no contenerlo, asumiendo que esta lista esta ordenada, Si hay 1000 elementos, el tamaño baja 1000 -> 500 -> 250 ... hasta encontrarlo, por lo que  la complejidad es de O(log n)
#¿En qué condiciones conviene usar cada uno?
    # R/
        #   - La lineal conviene cuando es una lista pequeña, o desordenada y cuando solo se va a buscar una vez
        #   - La binaria conviene cuando es una lista grande y ua se encuentra ordenada.
#¿Qué pasa si la lista no está ordenada?
    # R/
        #   - En linear_search sigue funcionando igual ya que esta no depende del orden y revisa valor por valor.
        #   - En binary_search dejaria de ser confiable, porque esta descarta la mitad asumiendo que la lista esta ordenada, si se descarta la mitad en una lista desordenada, corre el riesgo que elimine el objetivo y devolve False aunque si exista el valor