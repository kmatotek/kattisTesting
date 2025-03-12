from math import comb

def max_probability(n, p):
    # Initialize the maximum probability to 0
    max_prob = 0.0
    
    # Iterate over all possible values of k (how many times to add your name)
    for k in range(p + 1):
        # Calculate the total number of names including yours
        total_names = n + k
        
        # Calculate the probability of being drawn exactly once
        prob = comb(k, 1) * comb(n, p - 1) / comb(total_names, p)
        
        # Update the maximum probability if the current one is higher
        max_prob = max(max_prob, prob)
    
    return max_prob

# Example usage:
n, p = map(int, input().split())
result = max_probability(n, p)
print(f"{result:.6f}")