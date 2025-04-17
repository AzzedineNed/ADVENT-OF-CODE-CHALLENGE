# Open and read the input data from the file
with open("input1.txt") as fin:
    data = fin.read()

# Initialize the total distance to 0
total_distance = 0

# Lists to store the location IDs from both groups
left_list = []
right_list = []

# Parse each line of the input data and split the numbers into left and right lists
for line in data.strip().split("\n"):
    location_ids = [int(i) for i in line.split("   ")]  # Split by 3 spaces (adjust if needed)
    left_list.append(location_ids[0])  # Add to the left list
    right_list.append(location_ids[1])  # Add to the right list

# Sort both lists to pair the smallest numbers first
left_list.sort()
right_list.sort()

# Calculate the total distance by summing the absolute differences
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

# Output the total distance between the lists
print(total_distance)
