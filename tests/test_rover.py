import pytest

from mars_rover.rover import Orientation, Rover


@pytest.mark.parametrize(
    "starting_orientation,expected",
    [
        (Orientation.NORTH, Orientation.WEST),
        (Orientation.WEST, Orientation.SOUTH),
        (Orientation.SOUTH, Orientation.EAST),
        (Orientation.EAST, Orientation.NORTH),
    ],
)
def test_rover__turn_left(starting_orientation: Orientation, expected: Orientation):
    rover = Rover(0, 0, starting_orientation, "")
    actual = rover.turn_left()
    assert actual == expected


@pytest.mark.parametrize(
    "starting_orientation,expected",
    [
        (Orientation.NORTH, Orientation.EAST),
        (Orientation.WEST, Orientation.NORTH),
        (Orientation.SOUTH, Orientation.WEST),
        (Orientation.EAST, Orientation.SOUTH),
    ],
)
def test_rover__turn_right(starting_orientation: Orientation, expected: Orientation):
    rover = Rover(0, 0, starting_orientation, "")
    actual = rover.turn_right()
    assert actual == expected


@pytest.mark.parametrize(
    "orientation,expected_x,expected_y",
    [
        (Orientation.NORTH, 1, 2),
        (Orientation.EAST, 2, 1),
        (Orientation.SOUTH, 1, 0),
        (Orientation.WEST, 0, 1),
    ],
)
def test_rover__forward__located_in_middle_of_grid(orientation: Orientation, expected_x: int, expected_y: int):
    # assuming a 3x3 Grid
    rover = Rover(1, 1, orientation, "")
    rover.forward()
    assert (rover.x, rover.y) == (expected_x, expected_y)
