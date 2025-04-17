from collections import defaultdict

# Open and read the input data from the file
with open("input1.txt") as fin:
    data = fin.read()

# Initialize the similarity score to 0
similarity_score = 0

# Lists to store the location IDs from both groups
left_list = []
right_list = []

# Parse each line of the input data and split the numbers into left and right lists
for line in data.strip().split("\n"):
    location_ids = [int(i) for i in line.split("   ")]  # Split by 3 spaces (adjust if needed)
    left_list.append(location_ids[0])  # Add to the left list
    right_list.append(location_ids[1])  # Add to the right list

# Count the occurrences of each number in the right list using a defaultdict
right_counts = defaultdict(int)
for location_id in right_list:
    right_counts[location_id] += 1

# Calculate the similarity score by multiplying each number in the left list
# with its frequency in the right list and accumulating the result
for location_id in left_list:
    similarity_score += location_id * right_counts[location_id]

# Output the final similarity score
print(similarity_score)
