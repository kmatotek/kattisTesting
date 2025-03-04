n = int(input())
lowest_99 = (n//100)*100 + 99
highest_99 = lowest_99 + 99
if n < lowest_99:
    print(highest_99)
else:
    print(lowest_99)