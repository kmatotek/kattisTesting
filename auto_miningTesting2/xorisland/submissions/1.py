def number_of_meetings(n, hats):
    t, p = [0]*32, [0]*32
    xor = [0]*32

    for i in range(n):
        for j in range(25, -1, -1):
            if (((hats[i]>>j)&1) > 0):
                if (t[j] > 0):
                    xor[i] = max(xor[i], p[j] + 2)
                t[j], p[j] = t[j] + 1, i

    for i in range(n):
        for j in range(i + 1, n):
            if t[hats[i] ^ hats[j]] > 2:
                xor[i] = max(xor[i], 3)
                xor[j] = max(xor[j], 3)

    return max(xor)


n = int(input().strip())
hats = [int(input().strip()) for _ in range(n)]

print(number_of_meetings(n, hats))