from pathlib import Path

from mars_rover.input_parser import parse_input


def end_to_end_test(path: Path, expected: list[str], include_max_index_in_grid: bool):
    grid, rovers = parse_input(path, include_max_index_in_grid=include_max_index_in_grid)
    actual = []
    for rover in rovers:
        rover.attach_to_grid(grid)
        rover.run_commands()
        actual.append(str(rover))
    for index, row in enumerate(actual):
        assert row == expected[index]


def test_E2E_example1__max_index_included():
    end_to_end_test(
        Path("./tests/example_input1.txt"),
        [
            "(4, 4, E)",
            "(0, 4, W) LOST",
        ],
        include_max_index_in_grid=True,
    )


def test_E2E_example1__max_index_excluded():
    end_to_end_test(
        Path("./tests/example_input1.txt"),
        [
            "(3, 4, E) LOST",
            "(0, 4, W) LOST",
        ],
        include_max_index_in_grid=False,
    )


def test_E2E_example2():
    end_to_end_test(
        Path("./tests/example_input2.txt"),
        [
            "(2, 3, W)",
            "(1, 0, S) LOST",
        ],
        include_max_index_in_grid=True,
    )


def test_E2E_made_up_example__max_index_included():
    end_to_end_test(
        Path("./tests/example_input_made_up.txt"),
        [
            "(3, 2, E)",
            "(1, 1, W)",
            "(1, 3, N)",
        ],
        include_max_index_in_grid=True,
    )


def test_E2E_made_up_example__max_index_excluded():
    end_to_end_test(
        Path("./tests/example_input_made_up.txt"),
        [
            "(2, 2, E) LOST",
            "(1, 1, W)",
            "(1, 2, N) LOST",
        ],
        include_max_index_in_grid=False,
    )
