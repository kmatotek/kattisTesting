def count_groups_not_accepted():
    N, M = map(int, input().split())
    group_sizes = list(map(int, input().split()))
    
    groups_not_accepted = 0
    current_seats_available = N
    
    for group_size in group_sizes:
        if group_size > current_seats_available:
            groups_not_accepted += 1
        else:
            current_seats_available -= group_size
            
    print(groups_not_accepted)

count_groups_not_accepted()