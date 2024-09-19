import numpy as np

# Data input
data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

# Fungsi untuk menghitung jumlah tetangga
def sum_grid_cells(data):
    grid = np.array(data)
    rows, cols = grid.shape
    result = np.zeros_like(grid)
    
    for i in range(rows):
        for j in range(cols):
            # Horizontal
            horizontal_sum = np.sum(grid[i, :])
            # Vertical
            vertical_sum = np.sum(grid[:, j])
            # Diagonals
            diag1_sum = np.sum(np.diag(grid, j - i))
            diag2_sum = np.sum(np.diag(np.fliplr(grid), (cols - 1) - (j + i)))
            
            result[i, j] = (horizontal_sum + vertical_sum + diag1_sum + diag2_sum
                            - 3 * grid[i, j])  # Subtracting cell value thrice to avoid double counting

    return result


print(sum_grid_cells(data))