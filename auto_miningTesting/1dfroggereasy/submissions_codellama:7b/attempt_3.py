import sys

# Read input from standard input
n, s, m = map(int, input().split())
board = list(map(int, input().split()))

# Initialize variables
fate = None
hops = 0

# Loop until the fate is determined
while fate == None:
    # Check if the frog has reached the magic number
    if board[s] == m:
        fate = "magic"
        break
    
    # Check if the frog has fallen off the left end of the board
    elif s == 1:
        fate = "left"
        break
    
    # Check if the frog has fallen off the right end of the board
    elif s == n:
        fate = "right"
        break
    
    # Check if the frog is in a cycle
    elif board[s] < 0 and (board[s] + board[s+1]) % m == 0:
        fate = "cycle"
        break
    
    # Make the next hop
    hops += abs(board[s])
    s += board[s]
    
# Output the result
print(fate)
print(hops)