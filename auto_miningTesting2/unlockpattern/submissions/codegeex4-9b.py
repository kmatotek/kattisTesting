def calculate_distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def unlock_pattern_length(pivots):
    total_length = 0
    for i in range(len(pivots) - 1):
        x1, y1 = divmod((pivots[i] - 1), 3)
        x2, y2 = divmod((pivots[i + 1] - 1), 3)
        total_length += calculate_distance(x1, y1, x2, y2)
    return total_length

# Reading input
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))

pivots = line1 + line2 + line3

# Calculating unlock pattern length
length = unlock_pattern_length(pivots)

# Printing the result
print(f"{length:.10f}")