from mars_rover.grid import Grid
from mars_rover.rover import Orientation, Rover


def test_rover__forward__marks_lost__with_a_grid():
    grid = Grid(5, 5)
    rover = Rover(0, 0, Orientation.SOUTH, "")
    rover.attach_to_grid(grid)
    rover.forward()
    assert rover.is_lost


def test_rover__forward__does_not_change_position__when_lost():
    grid = Grid(5, 5)
    rover = Rover(0, 0, Orientation.SOUTH, "")
    rover.attach_to_grid(grid)
    x, y = rover.forward()
    assert (x, y) == (rover.x, rover.y)
