# Open the input file and read the puzzle input
with open("input4.txt") as fin:
    grid = fin.read().strip().split("\n")

# Get the dimensions of the grid
n = len(grid)  # Number of rows
m = len(grid[0])  # Number of columns

# Generate all possible directions to check for "MAS" in the shape of an X
directions = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:  # Skip (0,0) direction as it's not a valid direction
            directions.append((dx, dy))

# Function to check if an "X-MAS" is found at position (i, j)
def find_xmas_x_shape(i, j):
    # Ensure that (i, j) is within bounds to form an X
    if not (1 <= i < n - 1 and 1 <= j < m - 1):
        return False
    # The center of the X should be 'A'
    if grid[i][j] != "A":
        return False

    # Check both diagonals for "MAS"
    diag_1 = f"{grid[i-1][j-1]}{grid[i+1][j+1]}"  # Top-left to bottom-right diagonal
    diag_2 = f"{grid[i-1][j+1]}{grid[i+1][j-1]}"  # Top-right to bottom-left diagonal

    # Ensure both diagonals contain either "MS" or "SM" for valid X-MAS
    return diag_1 in ["MS", "SM"] and diag_2 in ["MS", "SM"]

# Count the total occurrences of X-MAS in the shape of an X
total_xmas_x_shape = 0
for i in range(n):
    for j in range(m):
        total_xmas_x_shape += find_xmas_x_shape(i, j)

# Output the total number of occurrences of X-MAS in the shape of an X
print(total_xmas_x_shape)
