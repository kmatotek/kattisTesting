def find_frames(D):
    # Iterate over possible values of n1
    for n1 in range(int(D**0.5) + 1):
        n2_squared = D + n1**2
        n2 = int(n2_squared**0.5)
        
        if n2 * n2 == n2_squared:
            return (n1, n2)
    
    # If no such pair is found, return "impossible"
    return "impossible"

# Input
D = int(input())

# Output the result
result = find_frames(D)
print(result)