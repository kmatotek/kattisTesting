def find_nearest(n):
    if str(n)[-2:] == '99':
        return n
    
    digit = int(str(n)[:-2]) + 1 if int(str(n)[-2:]) >= 50 else int(str(n)[:-2])

    return (digit * 100) - 1

n = int(input())
print(find_nearest(n))