# Versión 1:
def manual_add(n):
    result = 0
    for i in range(1, n + 1): # O(n)
        result += i
    return result

# Versión 2:
def add_formula(n):
    return n * (n + 1) // 2 # O(1)


#¿Cuál es la complejidad de cada versión?
    # R/ 
    #   - La version 1 tiene un ciclo por lo que da n cantidad de vueltas, lo que hace que sea O(n) mientra
    #   - La version 2 no contiene ciclos, solo realiza operaciones sin importar el tamaño lo que hhace que sea O(1)


#¿Qué versión usaría si n = 1 000 000 000? ¿Por qué?
    # R/
    #   - Ambas tienen el mismo resultado, pero la version 1 va a hacer muchisimas vueltas por el ciclo mientras que la version 2 hace las operaciones tardando lo que tarde n, por lo tanto usaria la version 2 ya que seria mas eficiente