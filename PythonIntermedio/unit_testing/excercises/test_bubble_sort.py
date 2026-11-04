import pytest
from PythonIntermedio.sort_algorithms.excercises.task_01 import bubble_sort

def test_bubble_sort_short_list():
    original_list = [18, -11, 68, 6, 32, 53, -2]
    expected = sorted(original_list)
    result = bubble_sort(original_list)
    assert result == expected

def test_bubble_sort_large_list_more_than_100_elements():
    original_list = [
    45, -12, 87, 3, 56, -78, 21, 94, -5, 33,
    67, -41, 12, 99, -23, 8, 76, -60, 15, 52,
    -90, 29, 64, -17, 81, 4, -35, 70, 38, -8,
    91, -52, 26, 59, -2, 73, -66, 18, 47, 100,
    -29, 62, 10, -84, 35, 77, -14, 55, 1, -47,
    83, -71, 24, 68, -9, 41, 96, -33, 14, 58,
    -56, 79, 6, -21, 49, 88, -63, 31, 72, -1,
    19, -95, 53, 85, -27, 43, 66, -38, 92, 7,
    -74, 25, 61, -15, 80, 36, -49, 97, 11, -68,
    50, 28, -82, 74, 16, -31, 63, 89, -6, 42,
    -44, 69, 22, -58, 78, 13, -25, 54, 95, -19,
]
    assert len(original_list) > 100
    expected = sorted(original_list)
    result = bubble_sort(original_list)
    assert result == expected

def test_bubble_sort_empty_list():
    assert bubble_sort([]) == []

def test_bubble_sort_not_working_with_params_that_are_not_a_list():
    not_list = True
    with pytest.raises(TypeError):
        bubble_sort(not_list)