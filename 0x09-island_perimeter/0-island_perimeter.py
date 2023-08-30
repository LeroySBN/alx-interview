#!/usr/bin/python3
""" module 0-island_perimeter contains function island_perimeter """


def island_perimeter(grid):
    """ island_perimeter returns the perimeter of the island described in grid

    Args:
        grid (list): a list of lists of integers:
            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
            Cells are connected horizontally/vertically (not diagonally).
            grid is rectangular, with its width and height not exceeding 100
    Returns:
        int: the perimeter of the island described in grid
    """
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                perimeter += 4
                if row > 0 and grid[row - 1][col]:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1]:
                    perimeter -= 2
    return perimeter
