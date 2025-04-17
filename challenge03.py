import re

# Read the corrupted memory input
with open("input3.txt") as fin:
    corrupted_memory = fin.read().strip()

# Find all valid multiplication instructions (mul(X,Y))
valid_multiplications = re.findall(r"mul\((\d+),(\d+)\)", corrupted_memory)

# Initialize the total sum of valid multiplication results
total_sum = 0

# Loop through each valid multiplication instruction
for multiplication in valid_multiplications:
    # Multiply the two numbers and add to the total sum
    total_sum += int(multiplication[0]) * int(multiplication[1])

# Print the total sum of valid multiplications
print(total_sum)
