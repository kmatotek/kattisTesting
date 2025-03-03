def cinema_visitors():
    N, M = map(int, input().split())
    groups = list(map(int, input().split()))
    
    total = 0
    rejected = 0
    for group in groups:
        if total + group > N:
            rejected += 1
        else:
            total += group
            
    return rejected

print(cinema_visitors())