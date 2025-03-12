def noOfPosNumbers(T, d_cases):
    MOD = 1000000007
    output = []
    
    for i in range(T):
        count = pow(8, d_cases[i], MOD)
        output.append(count)

    return output

# Testing the function
T = 2
d_cases = [2, 3]
print(noOfPosNumbers(T, d_cases))