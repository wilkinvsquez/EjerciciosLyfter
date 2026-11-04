import operations, pytest
class TestAddition:
    def test_addition_with_strings(self):
        with pytest.raises(TypeError, match="Existen valores no numericos"):
                operations.addition([10, "Hola", 30])

    def test_empty_list(self):
        assert operations.addition([]) == 0

    def test_floats_and_negatives(self):
        assert operations.addition([1.5, -2.5, 4.0])== 3.0

class TestAverage:
    def test_average_with_strings(self):
        with pytest.raises(TypeError, match="Existen valores no numericos"):
                operations.average([10, "Hola", 30])

    def test_average_empty_list(self):
        with pytest.raises(ValueError, match="La lista no puede estar vacia"):
                        operations.average([])

    def test_average_floats_and_negatives(self):
        assert operations.average([1.5, -2.5, 4.0]) == pytest.approx(1.0)


class TestConvertion:
    def test_convertion_with_strings(self):
        with pytest.raises(TypeError, match="El valor a convertir no es numerico"):
                operations.celsius_a_fahrenheit("Test")

    def test_convertion_floats_and_negatives(self):
        assert operations.celsius_a_fahrenheit(-12.5) == pytest.approx(9.5)

    def test_convertion_with_integers(self):
            assert operations.celsius_a_fahrenheit(28) == 82.4