import math

def calculate_distance(commands_count, movements):
    """Calculates the straight-line distance from the starting position to the final position of the turtle.

    Args:
        commands_count: The number of commands.
        movements: A list of commands for the turtle.

    Returns:
        The distance from the starting position to the final position, rounded to the nearest integer.
    """
    x_pos, y_pos = 0, 0
    direction = 0  # Facing east

    for _ in range(commands_count):
        command = movements.pop(0).split()
        action = command[0]
        value = int(command[1]) if len(command) > 1 else 0

        if action == 'fd':
            x_pos += value * math.cos(math.radians(direction))
            y_pos += value * math.sin(math.radians(direction))
        elif action == 'bk':
            x_pos -= value * math.cos(math.radians(direction))
            y_pos -= value * math.sin(math.radians(direction))
        elif action == 'rt':
            direction = (direction + value) % 360
        elif action == 'lt':
            direction = (direction - value) % 360

    distance = round(math.sqrt(x_pos**2 + y_pos**2))
    return distance

def main():
    """Processes test cases for turtle movements."""
    test_cases = int(input())

    for _ in range(test_cases):
        commands_count = int(input())
        movements = [input() for _ in range(commands_count)]
        distance = calculate_distance(commands_count, movements)
        print(distance)

if __name__ == "__main__":
    main()