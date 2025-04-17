# Initialize the count for safe reports
safe_reports_count = 0

# Read the input file and split it into lines
with open("input2.txt") as fin:
    reports = fin.read().strip().split("\n")

# Function to check if a report is safe
def is_report_safe(levels):
    # Check if the sequence is increasing
    is_increasing = levels[1] > levels[0]
    
    # If increasing, check the differences between adjacent levels
    if is_increasing:
        for i in range(1, len(levels)):
            difference = levels[i] - levels[i-1]
            if not (1 <= difference <= 3):  # Difference must be between 1 and 3
                return False
        return True  # Safe if all differences are valid

    # If decreasing, check if the differences are between -3 and -1
    else:
        for i in range(1, len(levels)):
            difference = levels[i] - levels[i-1]
            if not (-3 <= difference <= -1):  # Difference must be between -3 and -1
                return False
        return True  # Safe if all differences are valid

# Loop through each report and check if it's safe
for report in reports:
    # Convert each line into a list of integers
    levels = [int(level) for level in report.split()]
    
    # Increment the safe report count if the report is safe
    safe_reports_count += is_report_safe(levels)

# Print the total number of safe reports
print(safe_reports_count)
