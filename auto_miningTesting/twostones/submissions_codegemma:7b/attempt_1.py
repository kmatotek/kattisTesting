def game_of_stones(n):
    if n % 2 == 1:
        return "Alice"
    else:
        return "Bob"

n = int(input())
print(game_of_stones(n))