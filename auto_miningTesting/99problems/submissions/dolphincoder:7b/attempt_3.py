def find_nearest(n):
    last_digit = n % 10
    if last_digit < 5 and str(n)[-2:] != '99':
        return (int(str(n)[:-2]) + 1) * 100 - 1
    
    if last_digit >= 5 and str(n)[-2:] != '99':
        return int(str(n)[:-2]) * 100
        
    return n

# Test the function with sample inputs and expected outputs
test_cases =  [(10, 99), (249, 299), (10000, 9999)]
for test_case in test_cases:
    actual_result = find_nearest(test_case[0])
    assert actual_result == test_case[1], f'Test case {test_case} failed with output {actual_result}'
print('All test cases passed!')