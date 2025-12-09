import csv
import os
from collections import deque


BASE_DIR = os.path.dirname(__file__)
input_path = os.path.join(BASE_DIR, "input.csv")

def get_grid():
    grid = []
    with open(input_path, newline="\n") as f:
        reader = csv.reader(f)
        for row in reader:
            curr = [c for c in row[0]]
            grid.append(curr)
    return grid

def can_lift_roll(grid, row, col):
    adjacent_cells = [(-1, -1), (-1, 0), (-1, 1),
                       (0, -1), (0, 1), 
                       (1, -1), (1, 0), (1, 1)
    ]
    num_surrounding_rolls = 0

    for adjacent_cell_config in adjacent_cells:
        row_add, col_add = adjacent_cell_config
        adjacent_cell_row = row + row_add
        adjacent_cell_col = col + col_add

        if adjacent_cell_row not in range(0, len(grid)) or adjacent_cell_col not in range(0, len(grid[0])):
            continue

        num_surrounding_rolls += 1 if grid[adjacent_cell_row][adjacent_cell_col] == "@" else 0
    
    return num_surrounding_rolls < 4



def solution():
    grid = get_grid()
    num_rolls_accessible = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            curr_elem = grid[row][col]
            if curr_elem == "@" and can_lift_roll(grid, row, col):
                num_rolls_accessible += 1
    return num_rolls_accessible

print(solution())