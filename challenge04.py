# Open the input file and read the puzzle input
with open("input4.txt") as fin:
    grid = fin.read().strip().split("\n")

# Get the dimensions of the grid
n = len(grid)  # Number of rows
m = len(grid[0])  # Number of columns

# Generate all possible directions to search for the word "XMAS"
directions = []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:  # Skip (0,0) direction as it's not a valid direction
            directions.append((dx, dy))

# Function to check if "XMAS" can be found starting from grid[i][j] in direction d
def find_xmas(i, j, direction):
    dx, dy = direction
    # Check if "XMAS" fits in the grid starting from (i, j) in the given direction
    for k, char in enumerate("XMAS"):
        ii = i + k * dx  # Calculate new row index
        jj = j + k * dy  # Calculate new column index
        # Check if the new indices are out of bounds or if the character doesn't match
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        if grid[ii][jj] != char:
            return False
    return True

# Count the total occurrences of "XMAS" in all directions from every cell in the grid
total_xmas = 0
for i in range(n):
    for j in range(m):
        for direction in directions:
            total_xmas += find_xmas(i, j, direction)

# Output the total number of occurrences of "XMAS"
print(total_xmas)
