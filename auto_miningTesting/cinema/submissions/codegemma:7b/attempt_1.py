N, M = map(int, input().split())
sizes = list(map(int, input().split()))

count = 0
total = 0

for size in sizes:
    if total + size > N:
        count += 1
    else:
        total += size

print(count)