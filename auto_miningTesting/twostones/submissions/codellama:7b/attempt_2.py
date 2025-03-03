# Python program to determine the winner of a game of stones played by Alice and Bob

if __name__ == '__main__':
    # Read the number of stones from the input
    n = int(input())
    
    # Initialize variables to keep track of the winning condition
    odd_stone = False
    last_stone = 0
    
    # Iterate through the stones and check for consecutive stones
    for i in range(1, n + 1):
        if i == n or (i + 1) % 2 != 0:
            # If the current stone is odd, set the winning condition to Alice
            odd_stone = True
        elif last_stone == i - 1:
            # If the previous stone was also taken by the player, the game is a draw
            print("Draw")
            exit()
        else:
            # Set the last stone taken as the current stone
            last_stone = i
    
    if odd_stone:
        print("Alice")
    elif last_stone == n - 1:
        print("Draw")
    else:
        print("Bob")