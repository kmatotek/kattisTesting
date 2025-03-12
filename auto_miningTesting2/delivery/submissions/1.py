import sys, heapq

def postal_service(N, K, deliveries):
    left = []
    right = []
    deliveries = sorted(deliveries)
    for pos, letters in deliveries:
        if pos < 0:
            left.append((pos, letters))
        else:
            right.append((pos, letters))

    left = left[::-1]
    distance = 0
    while left:
        pos, letters = left.pop()
        distance += 2 * abs(pos) * ((letters + K - 1)//K)
        if letters % K != 0 and left and left[-1][1] <= K - letters % K:
            extra, = heapq.heappushpop(left, ((pos, letters%K)))
            left.append((pos, extra))
    
    while right:
        pos, letters = right.pop()
        distance += 2 * abs(pos) * ((letters + K - 1)//K)
        if letters % K != 0 and right and right[-1][1] <= K - letters % K:
            extra, = heapq.heappushpop(right, ((pos, letters%K)))
            right.append((pos, extra))

    return distance

def main():
    N, K = map(int, input().split())
    deliveries = [tuple(map(int, input().split())) for _ in range(N)]
    result = postal_service(N, K, deliveries)
    print(result)

if __name__ == "__main__":
    main()