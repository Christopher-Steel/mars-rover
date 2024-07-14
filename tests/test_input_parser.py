import pytest

from mars_rover.input_parser import (
    parse_commands,
    parse_first_line,
    parse_int,
    parse_orientation,
    parse_rover_line,
)
from mars_rover.rover import Orientation


@pytest.mark.parametrize(
    "string,expected,raises",
    [
        ("N", Orientation.NORTH, False),
        ("E", Orientation.EAST, False),
        ("S", Orientation.SOUTH, False),
        ("W", Orientation.WEST, False),
        ("X", None, True),
    ],
)
def test_parse_orientation(string: str, expected: Orientation | None, raises: bool):
    if raises:
        with pytest.raises(ValueError):
            parse_orientation(string)
    else:
        actual = parse_orientation(string)
        assert actual == expected


@pytest.mark.parametrize(
    "string,raises",
    [
        ("FLRFRFRFR", False),
        ("XXXX", True),
    ],
)
def test_parse_commands(string: str, raises: bool):
    if raises:
        with pytest.raises(ValueError):
            parse_commands(string)
    else:
        actual = parse_commands(string)
        assert actual == string


@pytest.mark.parametrize(
    "string,expected,raises",
    [
        ("5", 5, False),
        ("0", 0, False),
        ("  2 ", 2, False),
        ("E", None, True),
        ("2,", None, True),
    ],
)
def test_parse_int(string: str, expected: int | None, raises: bool):
    if raises:
        with pytest.raises(ValueError):
            parse_int(string)
    else:
        actual = parse_int(string)
        assert actual == expected


@pytest.mark.parametrize(
    "string,expected,raises",
    [
        ("1 2", (1, 2), False),
        ("1 2 3 ABC", None, True),
        ("0 1", None, True),
        ("1 0", None, True),
    ],
)
def test_parse_first_line(string: str, expected: tuple[int, int] | None, raises: bool):
    if raises:
        with pytest.raises(ValueError):
            parse_first_line(string)
    else:
        actual = parse_first_line(string)
        assert actual == expected


def test_parse_rover_line__raises__if_row_does_not_start_with_opening_parenthesis():
    with pytest.raises(ValueError):
        parse_rover_line("no parenthesis")


def test_parse_rover_line__raises__if_row_does_not_contain_one_closing_parenthesis():
    with pytest.raises(ValueError):
        parse_rover_line("(1, 2, E) (FRLLRF)")
