class Grid:
    def __init__(self, width: int, height: int, include_max_index: bool = False) -> None:
        # Intuitively for me an MxN grid should not include M or N. The first example output
        # for this exercise goes against that and includes 4 as a valid x coordinate for a 4x8 grid
        # I wasn't sure if this was an error or intentional so I made this configurable via CLI arg
        # and if that arg isn't passed it will default to the way the examples showed
        if include_max_index:
            width += 1
            height += 1
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Grid({self.width}x{self.height})"

    def contains(self, x: int, y: int) -> bool:
        return x >= 0 and x < self.width and y >= 0 and y < self.height
