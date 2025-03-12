def calc_distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

def calc_total_length(pivots):
    total_length = 0
    for i in range(len(pivots)):
        for j in range(i+1, len(pivots)):
            x1 = (pivots[i] - 1) % 3
            y1 = (pivots[i] - 1) // 3
            x2 = (pivots[j] - 1) % 3
            y2 = (pivots[j] - 1) // 3
            total_length += calc_distance(x1, y1, x2, y2)
    return total_length

if __name__ == "__main__":
    pivots = []
    for _ in range(3):
        line = list(map(int, input().split()))
        pivots.extend(line)

    print(calc_total_length(pivots))