def game_winner(n):
    if n % 2 == 0:
        return "Bob"
    else:
        return "Alice"

# read input from standard input
n = int(input().strip())
print(game_winner(n))