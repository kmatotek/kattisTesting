def number_of_meetings(n, hats):
    def find_trio(hats):
        for i in range(len(hats)):
            for j in range(i + 1, len(hats)):
                for k in range(j + 1, len(hats)):
                    if hats[i] ^ hats[j] == hats[k]:
                        return {hats[i], hats[j], hats[k]}
        return None

    trio = find_trio(hats)
    days = 0
    known = set()

    while not known:
        days += 1
        for hat in hats:
            if hat in trio and hat not in known:
                known.add(hat)

    return days

# Reading input
n = int(input().strip())
hats = []
for _ in range(n):
    hats.append(int(input().strip()))

# Calculating the result
result = number_of_meetings(n, hats)

# Printing the result
print(result)