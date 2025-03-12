def check(r, p, n):
    h = r*(r+1)//2 + max(0, p-r*(r+1)//2)
    return h>=n+1

def calculate_probability(n, p):
    left = 0
    right = 1
    
    while right - left > 1e-6:
        mid = (left + right)/2
        
        if check(p//mid, p, n):
            right = mid
        else:
            left = mid
    
    return right

n, p = map(int, input().strip().split())
print("{0:.6f}".format(calculate_probability(n, p)))