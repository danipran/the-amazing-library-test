import pytest
from the_amazing_library import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (0, 0, 0),
        (-2, 3, 1),
        (2, -3, -1),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
