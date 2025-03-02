# Read N and M
values = list(map(int, input().split()))
N, M = values[0], values[1]

# Read group sizes
group_sizes = list(map(int, input().split()))

total_visitors = 0
rejections = 0
for size in group_sizes:
    total_visitors += size
    if total_visitors > N:
        rejections += 1

print(rejections)