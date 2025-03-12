def max_speed(b, n, e, sb, sn, se, c):
    participants = [sb] * b + [sn] * n + [se] * e
    kayaks = sorted(c)
    num_kayaks = len(kayaks)
    speeds = []
    
    for i in range(num_kayacs // 2):
        speed1 = kayaks[i]
        speed2 = kayaks[num_kayacs - i - 1]
        max_speed = min(speed1 * (participants[0] + participants[-1]), speed1 * (participants[1] + participants[-2]))
        speeds.append(max_speed)
    
    return max(speeds)

# Reading input
b, n, e = map(int, input().split())
sb, sn, se = map(int, input().split())
c = list(map(int, input().split()))

# Calculating the result
result = max_speed(b, n, e, sb, sn, se, c)

# Printing the result
print(result)