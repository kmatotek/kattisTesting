def reorder_numbers(numbers, order):
    a, b, c = sorted(numbers)
    ordered_numbers = [0]*3
    for i in range(3):
        if order[i] == 'A': 
            ordered_numbers[i] = a
        elif order[i] == 'B': 
            ordered_numbers[i] = b
        else: 
            ordered_numbers[i] = c
    return ordered_numbers

numbers = list(map(int, input().split()))
order = input()
result = reorder_numbers(numbers, order)

print(' '.join(map(str,result)))