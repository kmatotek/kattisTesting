# Import necessary libraries
from collections import deque

# Function to check if all groups can be accepted into the theater with given seats
def can_enter(group_sizes, n):
    q = deque(group_sizes) # Initialize a queue with group sizes
    
    count = 0 # Keep track of the number of groups that cannot enter
    while q:
        size = q.popleft() # Get the next group size
        
        if len(q) + 1 <= n - size:
            # If there are enough empty seats to accommodate this group, it will be accepted
            count += 1
        elif q and size < q[0]:
            # If there aren't any more groups to check or the current group is smaller than the next one in line, we can leave
            break
    
    return count


# Main function to read input and call the can_enter function
def main():
    n, m = map(int, input().split())  # Read number of seats and number of groups from input
    group_sizes = list(map(int, input().split()))  # Read sizes of all visiting groups
    
    print(can_enter(group_sizes, n))


# Call the main function
if __name__ == '__main__':
    main()