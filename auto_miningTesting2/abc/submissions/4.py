def rearrange_numbers(numbers, order):
    sorted_numbers = sorted(numbers)
    mapping = {'A': 0, 'B': 1, 'C': 2}
    result = [sorted_numbers[mapping[char]] for char in order]
    return result

numbers = list(map(int,input().split()))
order = input()
print(' '.join(map(str, rearrange_numbers(numbers, order))))