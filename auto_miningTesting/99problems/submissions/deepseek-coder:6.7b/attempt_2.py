def nearest_ending_in_99(n):
    # If n ends in 1-50 or 99-100, subtract the last two digits from 100 and add them to n.
    if int(str(n)[-2:]) <= 50 or int(str(n)[-2:]) >= 99:
        return n - int(str(n)[-2:]) + 100
    
    else:  
        # If n ends in 51-98, subtract the last digit and add 100.
        return n - int(str(n)[-1]) + 100

# Read input from standard input using input() function.
N = int(input())
print(nearest_ending_in_99(N))