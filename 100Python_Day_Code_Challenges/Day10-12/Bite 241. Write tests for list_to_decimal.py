import pytest

from numbers_to_dec import list_to_decimal

            # Valid Input
@pytest.mark.parametrize(
    "arg, expected", [([0, 4, 2, 8], 428), ([1, 2], 12), ([3, 5, 1], 351)]
)
def ValidInput(arg, expected):
    assert list_to_decimal(arg) == expected

            # TypeError
def error_min():
    with pytest.raises(ValueError):
        list_to_decimal([-3, 2, 1])
def error_max():
    with pytest.raises(ValueError):
        list_to_decimal([2, 1, 10])

        # ValueError
def error_str():
    with pytest.raises(TypeError):
        list_to_decimal(["str", 2, 1])
def error_float():
    with pytest.raises(TypeError):
        list_to_decimal([1, 2, 3.6])
