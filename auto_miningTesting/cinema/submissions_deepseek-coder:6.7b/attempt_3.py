# Read N and M
values = list(map(int, input().split()))
N, M = values[0], values[1]

# Read group sizes
group_sizes = list(map(int, input().split()))

rejections = 0
total_visitors = 0
for size in group_sizes:
    if total_visitors + size > N:  # Check if adding current group will exceed the theater capacity
        rejections += 1
    else:
        total_visitors += size  # If not, add its size to the running total of visitors

print(rejections)