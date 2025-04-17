import re

# Read the corrupted memory input
with open("input3.txt") as fin:
    corrupted_memory = fin.read().strip()

# Find all valid instructions (mul(X,Y), do(), and don't())
instructions = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", corrupted_memory)

# Initially, all mul instructions are enabled
multiplication_enabled = True

# Initialize the total sum of enabled multiplications
total_sum = 0

# Loop through each instruction found
for instruction in instructions:
    # If it's a multiplication instruction and it's enabled, perform the multiplication
    if instruction[2] == "" and multiplication_enabled:
        total_sum += int(instruction[0]) * int(instruction[1])
    else:
        # If it's a do() instruction, enable mul instructions
        if instruction[2] == "do()":
            multiplication_enabled = True
        # If it's a don't() instruction, disable mul instructions
        elif instruction[2] == "don't()":
            multiplication_enabled = False

# Print the total sum of the results from enabled multiplications
print(total_sum)
