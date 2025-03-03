def count_rejected_groups(n, m, group_sizes):
    seats_remaining = n
    rejected_count = 0

    for size in group_sizes:
        if size <= seats_remaining:
            seats_remaining -= size
        else:
            rejected_count += 1

    return rejected_count


# Reading input from stdin
n, m = map(int, input().strip().split())
group_sizes = list(map(int, input().strip().split()))

# Get the result
result = count_rejected_groups(n, m, group_sizes)

# Writing output to stdout
print(result)