#!/usr/bin/python3
""" Perimeter of an island """


def island_perimeter(grid):
    """ Function that returns the perimeter
    of the island described in the grid """
    p = 0
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if (grid[a][b] == 1):
                if (a <= 0 or grid[a - 1][b] == 0):
                    p += 1
                if (a >= len(grid) - 1 or grid[a + 1][b] == 0):
                    p += 1
                if (b <= 0 or grid[a][b - 1] == 0):
                    p += 1
                if (b >= len(grid[a]) - 1 or grid[a][b + 1] == 0):
                    p += 1
    return p
