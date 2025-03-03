# Read input values
N, M = map(int, input().split())
groups = list(map(int, input().split()))

# Initialize variables
seats_available = N
groups_not_accepted = 0

# Process each group in order
for group_size in groups:
    if group_size <= seats_available:
        seats_available -= group_size
    else:
        groups_not_accepted += 1

# Output the number of groups not accepted
print(groups_not_accepted)