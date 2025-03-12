def min_distance(N, K, deliveries):
    pos_deliveries = sorted([x for x in deliveries if x[0]>0], key=lambda x: x[0])
    neg_deliveries = sorted([x for x in deliveries if x[0]<0], key=lambda x: -x[0])
    total_distance = 0
    while pos_deliveries or neg_deliveries:
        total_distance += deliver(K, pos_deliveries)
        total_distance += deliver(K, neg_deliveries)
    return total_distance*2

def deliver(K, deliveries):
    letters_delivered = 0
    max_distance = 0
    while deliveries and letters_delivered + deliveries[-1][1] <= K:
        x, t = deliveries.pop()
        letters_delivered += t
        max_distance = abs(x)
    return max_distance

N, K = map(int,input().split())
deliveries = [list(map(int, input().split())) for _ in range(N)]
print(min_distance(N, K, deliveries))