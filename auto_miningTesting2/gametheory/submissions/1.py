def soccat_game():
    data_sets = int(input())
    results = []
    for _ in range(data_sets):
        number_cells = int(input())
        cells = list(map(int, input().split()))
        scores = list(map(int, input().split()))
        result_set = []
        dp = [0] * number_cells
        intervals = [[] for _ in range(number_cells)]
        for i in range(number_cells-1, -1, -1):
            p = cells[i]
            j = i + p
            while j < number_cells:
                if len(intervals[j]) == 0 or intervals[j][0][0] != j + intervals[j][0][1] * p:
                    dp[i] = max(dp[i], intervals[j][0][0] - j * p + dp[j] if len(intervals[j]) > 0 else 0)
                    break
                dp[i] = max(dp[i], intervals[j][0][2] + dp[intervals[j][0][3]] if len(intervals[j]) > 0 else 0)
                j += intervals[j][0][1] * p
            dp[i] += scores[i]
            while len(intervals[i]) > 0 and intervals[i][-1][2] < dp[i]:
                intervals[i].pop()
            intervals[i].append((i+j, (j-i)//p, dp[i], j))
        results.append(dp)
    for result in results:
        print(' '.join(str(x) for x in result))

soccat_game()