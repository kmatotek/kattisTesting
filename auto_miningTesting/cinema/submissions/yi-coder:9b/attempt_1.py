# Read input data
N, M = map(int,input().split())
groups = list(map(int,input().split()))

# Initialize counter of rejected groups and available seats
rejected_groups = 0
seats_left = N

for group in groups:
    if group > seats_left:
        rejected_groups += 1
    else:
        seats_left -= group

print(rejected_groups)