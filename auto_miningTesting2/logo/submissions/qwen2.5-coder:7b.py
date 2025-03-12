def calculate_distance(commands):
    x = y = angle = 0

    for command in commands:
        parts = command.split()
        action = parts[0]
        value = int(parts[1])

        if action == 'fd':
            angle_rad = (angle + 90) * (3.141592653589793 / 180)
            x += value * cos(angle_rad)
            y += value * sin(angle_rad)
        elif action == 'bk':
            angle_rad = (angle + 90) * (3.141592653589793 / 180)
            x -= value * cos(angle_rad)
            y -= value * sin(angle_rad)
        elif action == 'lt':
            angle += value
        elif action == 'rt':
            angle -= value

    return round((x ** 2 + y ** 2) ** 0.5)

def solve():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    results = []

    while index < len(data):
        test_cases = int(data[index])
        index += 1

        for _ in range(test_cases):
            num_commands = int(data[index])
            index += 1

            commands = []
            for _ in range(num_commands):
                commands.append(data[index])
                index += 1

            results.append(calculate_distance(commands))

    for result in results:
        print(result)

if __name__ == "__main__":
    solve()