from math import comb

def election_outcome(test_cases):
    for t in test_cases:
        N, V1, V2, W = t
        M = V1 + V2
        if V1 > N // 2:
            print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
        elif V2 > N // 2:
            print("RECOUNT!")
        else:
            prob = 0
            for k in range(N - M + 1):
                if V1 + k > V2 + (N - M - k):
                    prob += comb(N - M, k) * (0.5 ** (N - M))
            if prob > W / 100:
                print("GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!")
            elif prob == 0:
                print("RECOUNT!")
            else:
                print("PATIENCE, EVERYONE!")

# Test the function
test_cases = [(50, 25, 24, 50), (50, 24, 25, 50), (50, 27, 22, 70)]
election_outcome(test_cases)