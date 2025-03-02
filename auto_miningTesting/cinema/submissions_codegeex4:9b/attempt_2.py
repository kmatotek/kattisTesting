def groups_not_accepted():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    group_sizes = list(map(int, data[2:2+M]))
    
    count = 0
    current_seats = 0
    
    for size in group_sizes:
        if current_seats + size > N:
            count += 1
        else:
            current_seats += size
    
    print(count)