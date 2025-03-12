import sys
from math import factorial as fact

def main():
    # Read input values
    n, p = map(int, sys.stdin.read().split())
    
    # Calculate the maximum probability of winning exactly p prizes
    num = 1
    den = 1
    
    # Compute the numerator (n + p - 1) * (n + p - 2) * ... * n
    for i in range(n, n + p - 1, -1):
        num *= i
    
    # Compute the denominator p! * (n + p)! / (p * (n + p - p))
    den *= fact(p)
    den *= fact(n + p) // (fact(p) * fact(n))
    
    # Calculate the probability
    prob = num / den
    
    # Print the result with a precision of 10 decimal places
    print(f"{prob:.10f}")

if __name__ == "__main__":
    main()