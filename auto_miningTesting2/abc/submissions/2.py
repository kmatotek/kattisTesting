def rearrange_numbers():
    numbers = list(map(int, input().split()))
    order = list(input().strip())
    numbers.sort()
    mapping = {'A': numbers[0], 'B': numbers[1], 'C': numbers[2]}
    result = [str(mapping[i]) for i in order]
    print(' '.join(result))

rearrange_numbers()