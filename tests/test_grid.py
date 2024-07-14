import pytest

from mars_rover.grid import Grid


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (0, 0, True),
        (4, 4, True),
        (4, 2, True),
        (2, 4, True),
        (2, 2, True),
        (-1, 2, False),
        (2, -1, False),
        (5, 2, False),
        (2, 5, False),
    ],
)
def test_grid__contains(x: int, y: int, expected: bool):
    grid = Grid(5, 5)
    actual = grid.contains(x, y)
    assert actual == expected
