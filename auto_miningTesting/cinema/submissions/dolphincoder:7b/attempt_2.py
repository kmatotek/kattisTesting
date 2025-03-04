from collections import deque


def can_enter(group_sizes, n):
    q = deque(group_sizes)  # Initialize a queue with group sizes
    
    count = 0  # Keep track of the number of groups that cannot enter
    while q:
        size = q.popleft()  # Get the next group size
        
        if len(q) + 1 <= n - size:
             # If there are enough empty seats to accommodate this group, it will be accepted
            count += 1
        elif q and size < q[0]:
             # If there aren't any more groups to check or the current group is smaller than the next one in line, we can leave
            break
    
    return count


def main():
    n, m = map(int, input().split())   # Read number of seats and number of groups from input
    if n < 1 or n > 100:
        print('Invalid value for n')
        return
    
    group_sizes = list(map(int, input().split()))[:m]
    if m < 1 or m > 50:
        print('Invalid value for m')
        return

    for size in group_sizes:
        if size < 1 or size > 10:
            print('Invalid group size')
            return
    
    print(can_enter(group_sizes, n))


if __name__ == '__main__':
    main()