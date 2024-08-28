#!/usr/bin/python3
'''
solution
'''


def island_perimeter(grid):
    '''
        island perimeter algo
    '''
    row_length = len(grid)
    col_length = len(grid[0])
    perimeter = 0

    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == 1:
                perimeter += 4
                if i < row_length - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2
                if j < col_length - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2
    return perimeter
