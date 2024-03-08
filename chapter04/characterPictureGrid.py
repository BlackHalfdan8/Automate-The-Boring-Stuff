def rotate_grid_clockwise(grid):
    # Determine the dimensions of the original grid
    rows = len(grid)
    columns = len(grid[0])

    # Create a new grid with swapped dimensions
    rotated_grid = [[' ' for _ in range(rows)] for _ in range(columns)]

    # Loop through the original grid and populate the rotated grid
    for i in range(rows):
        for j in range(columns):
            rotated_grid[j][rows - 1 - i] = grid[i][j]

    return rotated_grid

# Example usage:
grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

rotated_result = rotate_grid_clockwise(grid)

# Print the rotated grid
for row in rotated_result:
    print(' '.join(row))
