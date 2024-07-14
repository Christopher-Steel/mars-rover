from argparse import ArgumentParser
from pathlib import Path

from mars_rover.input_parser import parse_input


def main() -> None:
    parser = ArgumentParser(prog="run_mars_rover.sh")
    parser.add_argument("path_to_input_file", type=str, help="The URL that the crawler will start crawling from")
    parser.add_argument(
        "-e",
        "--exclude-max-index-from-grid",
        action="store_true",
        help="By default a 4x4 grid accepts coordinates in [0, 4]. With this flag that changes to [0, 4)",
    )
    args = parser.parse_args()
    include_max_index_in_grid = not args.exclude_max_index_from_grid
    path_to_input_file = Path(args.path_to_input_file)

    grid, rovers = parse_input(path_to_input_file, include_max_index_in_grid=include_max_index_in_grid)

    for rover in rovers:
        rover.attach_to_grid(grid)
        rover.run_commands()
        print(str(rover))
