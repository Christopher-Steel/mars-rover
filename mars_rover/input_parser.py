from pathlib import Path

from mars_rover.grid import Grid
from mars_rover.rover import Orientation, Rover


def parse_first_line(line: str) -> tuple[int, int]:
    parts = line.split(" ")
    if len(parts) != 2:
        raise ValueError(f"The first line of input needs to be 'GRID_SIZE_X GRID_SIZE_Y'. Received '{line}'")
    width, height = parse_int(parts[0]), parse_int(parts[1])
    if width <= 0:
        raise ValueError(f"Grid width must be 1 or more, received {width}")
    if height <= 0:
        raise ValueError(f"Grid height must be 1 or more, received {height}")
    return width, height


def parse_int(string: str) -> int:
    string = string.strip()
    if not string.isnumeric():
        raise ValueError(f"'{string}' is not a valid number")
    return int(string)


def parse_orientation(string: str) -> Orientation:
    LETTER_TO_ORIENTATION = {
        "N": Orientation.NORTH,
        "E": Orientation.EAST,
        "S": Orientation.SOUTH,
        "W": Orientation.WEST,
    }
    string = string.strip()
    if string not in LETTER_TO_ORIENTATION:
        raise ValueError(f"'{string}' is not a valid orientation (N, E, S, W accepted)")
    return LETTER_TO_ORIENTATION[string]


def parse_commands(string: str) -> str:
    string = string.strip()
    for c in string:
        valid_commands = "FLR"
        if c not in valid_commands:
            raise ValueError(f"{c} is not a valid command, '{valid_commands}' accepted")
    return string


def parse_rover_line(line: str) -> tuple[tuple[int, int, Orientation], str]:
    if not line[0] == "(":
        raise ValueError(f"First character of a rover row must be '(', was '{line[0]}'")
    line = line[1:]  # Remove the opening parenthesis
    parts = line.split(")")
    if len(parts) != 2:
        raise ValueError(f"There must be only one ')' on a rover row, found {len(parts) - 1}")
    initial_position_str, commands_str = parts
    parts = initial_position_str.split(", ")

    x = parse_int(parts[0])
    y = parse_int(parts[1])
    orientation = parse_orientation(parts[2])
    commands = parse_commands(commands_str)
    return (x, y, orientation), commands


def parse_input(input_file: Path, **flags: bool) -> tuple[Grid, list[Rover]]:
    include_max_index_in_grid = flags.get("include_max_index_in_grid") or False
    rovers: list[Rover] = []
    with input_file.open("r") as f:
        first_line = f.readline().strip()
        width, height = parse_first_line(first_line)
        grid = Grid(width, height, include_max_index=include_max_index_in_grid)
        for line in f:
            (x, y, orientation), commands = parse_rover_line(line)
            rovers.append(Rover(x, y, orientation, commands))
    return grid, rovers
