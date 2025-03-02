# Read input from standard input
N, M = map(int, input().split())
groups = list(map(int, input().split()))

# Initialize variables
total_groups_not_accepted = 0
current_seats_available = N

# Iterate through each group and check if they can enter the theater
for group_size in groups:
    if group_size <= current_seats_available:
        current_seats_available -= group_size
    else:
        total_groups_not_accepted += 1

# Output the number of groups that will not be accepted
print(total_groups_not_accepted)