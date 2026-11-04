import pytest
from operations import read_lines
from unittest.mock import patch, mock_open


class TestFile:
    def test_read_lines_returns_expected_lines(self):
        test_text = "Hola\nMundo\ntest\n"

        with patch("builtins.open", mock_open(read_data = test_text)) as mocked_file:
            result = read_lines("file_test.txt")

        assert result == ["Hola\n", "Mundo\n", "test\n"]
        mocked_file.assert_called_once_with("file_test.txt", "r")

    def test_read_lines_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with pytest.raises(FileNotFoundError):
                read_lines("no/existe.txt")
