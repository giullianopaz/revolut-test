import pytest
from main import sum_int


@pytest.mark.parametrize(['a', 'b', 'expected'], [
    (1, 3, 4),
    (10, 3, 13),
    (111, 5, 116),
])
def test_sum_int(a, b, expected):
    assert sum_int(a, b) == expected
    