def determine_winner(n):
    if n % 2 == 1:
        return "Alice"
    else:
        return "Bob"

# Read input from standard input
n = int(input().strip())

# Determine the winner based on the number of stones
winner = determine_winner(n)

# Output the winner
print(winner)