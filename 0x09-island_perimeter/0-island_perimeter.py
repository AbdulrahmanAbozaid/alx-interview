#!/usr/bin/python3
"""
Island Perimeter
"""


def is_inside(i, j, grid):
    """check i, j are in the grid"""
    if (i < 0 or j < 0):
        return False

    if (j >= len(grid[0]) or i >= len(grid)):
        return False

    return True


def cell_perim(grid, cell):
    """Calc ground cell perimeter"""
    sides = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cnt = 0
    for side in sides:
        l_side = cell[0]+side[0]
        r_side = cell[1]+side[1]
        cnt += int(not is_inside(l_side, r_side, grid) or
                   (is_inside(l_side, r_side, grid)
                   and not grid[l_side][r_side]))

    return cnt


def island_perimeter(grid):
    """Give island perimeter

    Args:
        grid (List[List]): the island grid

    Returns:
        (int): the perimeter
    """
    if (len(grid) <= 0):
        return 0

    perim = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perim += cell_perim(grid, (i, j))

    return perim
