# Mars Rover

Tool to calculate final positions of Mars rovers given a trajectory string and an initial position within a specified area grid.

- **Github repository**: <https://github.com/Christopher-Steel/mars-rover/>

## How to use this tool

```bash
$> make install # If this is your first run
$> ./run_mars_rover.sh path_to_input_file [--exclude-max-index-from-grid]
```

## How to run tests

```bash
$> make test
```

## Flags

| Flag                          | Explanation                                                      |
| ----------------------------- | ---------------------------------------------------------------- |
| --exclude-max-index-from-grid | see [#exclude-max-index-from-grid](#exclude-max-index-from-grid) |

## Input file format

```
<X> <Y>
(<X>, <Y>, <ORIENTATION>) <COMMAND_SEQUENCE>
[...]
(<X>, <Y>, <ORIENTATION>) <COMMAND_SEQUENCE>
```

- <X> and <Y> are integers representing the grid size on the first row and coordinates within that grid on subsequent rows
- <ORIENTATION> is a single letter in N, E, S or W
- <COMMAND_SEQUENCE> is any number of letters in FLR
- The first row represents the size of the grid within which our robots will navigate.
- Each subsequent row represents a robot with its position (x, y), and its orientation (N, E, S, W)
- Each robot can move forward one space (F), rotate left by 90 degrees (L), or rotate
  right by 90 degrees (R)
- If a robot moves off the grid, it is marked as ‘lost’ and its last valid grid position and
  orientation is recorded
- Going from x -> x + 1 is in the easterly direction, and y -> y + 1 is in the northerly
  direction. i.e. (0, 0) represents the south-west corner of the grid

## exclude-max-index-from-grid

Intuitively for me an MxN grid should not include M or N.

The first example output for this exercise goes against that and includes 4 as a valid x coordinate for a 4x8 grid.

I wasn't sure if this was an error or intentional so I made this configurable via this CLI flag and if that flag isn't passed it will default to the way the examples showed.
