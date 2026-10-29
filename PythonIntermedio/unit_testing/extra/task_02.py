from operations import divide
import pytest

class TestDivide:
    def test_divide_by_2(self):
        assert divide(10,2) == 5.0

    def test_divide_by_0(self):
        with pytest.raises(ValueError):
            divide(10,0)

    def test_divide_by_string(self):
        with pytest.raises(TypeError):
            divide(10,"cero")