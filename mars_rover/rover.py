from enum import IntEnum

from mars_rover.grid import Grid


class Orientation(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Rover:
    def __init__(self, x: int, y: int, orientation: Orientation, commands: str) -> None:
        self.x = x
        self.y = y
        self.orientation = orientation
        self.commands = commands
        self.is_lost = False
        self.grid: Grid | None = None

    def __repr__(self) -> str:
        return f"Rover({self.x}, {self.y}, {self.orientation}, '{self.commands}')"

    def __str__(self) -> str:
        ORIENTATION_TO_LETTER = {
            Orientation.NORTH: "N",
            Orientation.EAST: "E",
            Orientation.SOUTH: "S",
            Orientation.WEST: "W",
        }
        return f"({self.x}, {self.y}, {ORIENTATION_TO_LETTER[self.orientation]}){" LOST" if self.is_lost else ""}"

    def run_commands(self) -> None:
        COMMAND_FNS = {"F": self.forward, "L": self.turn_left, "R": self.turn_right}
        for c in self.commands:
            COMMAND_FNS[c]()
            if self.is_lost:
                break

    def attach_to_grid(self, grid: Grid) -> None:
        self.grid = grid

    def forward(self) -> tuple[int, int]:
        match self.orientation:
            case Orientation.NORTH:
                new_pos = [self.x, self.y + 1]
            case Orientation.EAST:
                new_pos = [self.x + 1, self.y]
            case Orientation.SOUTH:
                new_pos = [self.x, self.y - 1]
            case Orientation.WEST:
                new_pos = [self.x - 1, self.y]
        if self.grid is None or self.grid.contains(*new_pos):
            self.x = new_pos[0]
            self.y = new_pos[1]
        else:
            self.is_lost = True
        return (self.x, self.y)

    def turn_left(self) -> Orientation:
        if not self.is_lost:
            new_ori = Orientation((self.orientation + len(Orientation) - 1) % len(Orientation))
            self.orientation = new_ori
        return self.orientation

    def turn_right(self) -> Orientation:
        if not self.is_lost:
            new_ori = Orientation((self.orientation + 1) % len(Orientation))
            self.orientation = new_ori
        return self.orientation
