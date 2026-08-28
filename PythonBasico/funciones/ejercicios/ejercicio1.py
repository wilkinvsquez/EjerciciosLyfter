# Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.


def print_test_text_second():
    print("This is the second test function")

def print_test_text_first ():
    print("This is a first test function")
    print_test_text_second()

print_test_text_first()