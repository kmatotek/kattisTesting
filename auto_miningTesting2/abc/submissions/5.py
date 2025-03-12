def rearrange(a, b, c, order):
    arr = [a, b, c]
    arr.sort()

    result = []
    for ch in order:
        if ch == 'A':
            result.append(str(arr[0]))
        elif ch == 'B':
            result.append(str(arr[1]))
        else: 
            result.append(str(arr[2]))

    return ' '.join(result)

a, b, c = map(int, input().strip().split())
order = input().strip()
print(rearrange(a, b, c, order))