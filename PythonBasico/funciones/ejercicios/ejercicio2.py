# Experimente con el concepto de scope:
# Intente acceder a una variable definida dentro de una función desde afuera.
# Intente acceder a una variable global desde una función y cambiar su valor.

# 2.1 
print("_______ 2.1 _______")
def test_function ():
    local_variable = 5

print(local_variable)


# 2.2
print("_______ 2.2 _______")
global_variable = 25

def change_value ():
    global_variable = 3

change_value()
print(global_variable)