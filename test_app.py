import pytest
from app import add


@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (-1, 1, 0)])
def test_add(a, b, expected):
    result = add(a, b)
    print(f"add({a}, {b}) = {result}")
    assert result == expected
