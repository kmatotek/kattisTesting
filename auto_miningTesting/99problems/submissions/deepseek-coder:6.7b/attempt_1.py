def nearest_ending_in_99(n):
    # If n ends in 50-99, add 49 to n and return the result.
    if (100 - int(str(n)[-2:])) <= 49:
        return n + 49
    
    else:  
        return n + (100 - 1 - int(str(n)[-2:])) # Else, add the difference to n and return the result.

# Read input from standard input using input() function.
N = int(input())
print(nearest_ending_in_99(N))