import pytest
from PythonBasico.funciones.ejercicios.ejercicio3 import sum_list_numbers
from PythonBasico.funciones.ejercicios.ejercicio4 import reverse_string
from PythonBasico.funciones.ejercicios.ejercicio5 import count_capitals_text,format_capitals_message
from PythonBasico.funciones.ejercicios.ejercicio6 import separate_and_sort
from PythonBasico.funciones.ejercicios.ejercicio7 import find_prime_numbers

# task 3 - sum_list_numbers
def test_list_of_numbers_adition():
    assert sum_list_numbers([4, 6, 2, 29]) == 41

def test_sum_list_numbers_with_empty_list():
    assert sum_list_numbers([]) == 0

def test_sum_list_numbers_with_non_numeric_elements():
    with pytest.raises(TypeError):
        sum_list_numbers([1,"a"])

# task 4 - reverse_string
def test_turn_a_string_backwards():
    assert reverse_string("Hola Mundo") == "odnuM aloH"

def test_turn_a_string_backwards_with_not_string_value():
    with pytest.raises(TypeError):
        reverse_string(123451)

def test_turn_a_string_backwards_with_numbers_and_simbols():
    assert reverse_string("abc123!") == "!321cba"

# task 5 - count_capitals_text
def test_upper_case_counter():
    assert count_capitals_text("I love Nación Sushi") == (3, 13)

def test_count_capitals_text_with_not_string_value():
    with pytest.raises(TypeError):
        count_capitals_text(["A", "b"])

def test_format_capitals_message():
    assert format_capitals_message(3, 13) == "There's 3 upper cases and 13 lower cases"

# task 6 - separate_and_sort
def test_sort_hyphen_separated_words_alphabetically():
    assert separate_and_sort("arca-computadora-funcion-perro-monitor-python-variable") == "arca-computadora-funcion-monitor-perro-python-variable"

def test_sort_hyphen_separated_words_alphabetically_with_not_string_value():
    with pytest.raises(AttributeError):
        separate_and_sort(123)

def test_sort_hyphen_separated_words_alphabetically_with_numbers_in_text():
    assert separate_and_sort("casa2-casa1-casa10") == "casa1-casa10-casa2"

# task 7 - find_prime_numbers, is_prime_number
def test_get_prime_numbers_from_list_with_mixed_numbers():
    assert find_prime_numbers([1, 4, 6, 7, 13, 9, 67]) == [7, 13, 67]

def test_get_prime_numbers_from_list_with_empty_list():
    assert find_prime_numbers([]) == []

def test_get_prime_numbers_from_list_with_not_list_value():
    with pytest.raises(TypeError):
        find_prime_numbers(None)