def find_frames(D):
    n1 = 0
    while True:
        n2 = n1 + 1
        if n2 * n2 - n1 * n1 > D:
            return "impossible"
        elif n2 * n2 - n1 * n1 == D:
            return n1, n2
        else:
            n1 += 1


D = int(input())
n1, n2 = find_frames(D)
if n1 == "impossible":
    print("impossible")
else:
    print(n1, n2)