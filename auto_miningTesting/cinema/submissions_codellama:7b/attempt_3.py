# Read input from standard input
n = int(input())
m = int(input())
group_sizes = list(map(int, input().split()))

# Calculate the number of groups that will not be accepted to the showing
num_groups = 0
for group_size in group_sizes:
    if group_size > n:
        num_groups += 1

print(num_groups)