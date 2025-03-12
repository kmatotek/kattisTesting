def max_kayak_speed(b, n, e, sb, sn, se, c):
    participants = sorted([sb]*b + [sn]*n + [se]*e)
    kayaks = sorted(c)

    # Initialize the total speed to 0
    total_speed = 0

    # Distribute participants and calculate the total speed
    for i in range(len(kayaks)):
        if i < b:
            total_speed += (participants[i] + participants[b+i]) * kayaks[i]
        elif i < b+n:
            total_speed += (participants[b+n+i-b-1] + participants[b+n+i]) * kayaks[i]
        else:
            total_speed += (participants[-2] + participants[-1]) * kayaks[i]

    # Return the maximum speed
    return max(kayaks) * (sum(participants[:b]) + sum(participants[b:b+n]) + sum(participants[-n:]))

# Read input values
b, n, e = map(int, input().split())
sb, sn, se = map(int, input().split())
c = list(map(int, input().split()))

# Print the maximum speed of the slowest kayak
print(max_kayak_speed(b, n, e, sb, sn, se, c))