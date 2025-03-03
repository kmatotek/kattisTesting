# Read input
N, M = map(int, input().split())
groups = list(map(int, input().split()))

# Initialize variables
total_visited = 0
rejected_groups = 0

# Process each group in order
for group_size in groups:
    if total_visited + group_size > N:
        rejected_groups += 1
    else:
        total_visited += group_size

# Output the number of rejected groups
print(rejected_groups)