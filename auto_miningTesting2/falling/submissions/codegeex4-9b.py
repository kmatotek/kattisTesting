def find_mug_frames(D):
    # Check if D is a perfect square
    if int(D**0.5)**2 != D:
        return "impossible"
    
    # Iterate over possible values of n1 and check if (n2^2 - n1^2) equals D
    for n1 in range(int(D**0.5)+1):
        n2 = int((D + n1*n1)**0.5)
        if n2**2 - n1**2 == D:
            return f"{n1} {n2}"
    
    # If no pair (n1, n2) is found, return "impossible"
    return "impossible"

# Read input
D = int(input().strip())

# Find the mug frames and print the result
result = find_mug_frames(D)
print(result)