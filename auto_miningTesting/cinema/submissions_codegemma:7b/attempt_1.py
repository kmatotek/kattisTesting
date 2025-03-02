# Read input
N, M = map(int, input().split())
groups = list(map(int, input().split()))

# Initialize count of rejected groups
rejected = 0

# Iterate through groups
for group in groups:
    # Check if there are enough seats
    if N >= group:
        N -= group
    else:
        rejected += 1

# Print output
print(rejected)