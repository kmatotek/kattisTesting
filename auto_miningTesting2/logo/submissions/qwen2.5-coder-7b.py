import math

def process_commands(commands):
    x, y = 0, 0
    angle = 0  # angle in degrees

    for command in commands:
        parts = command.split()
        cmd = parts[0]
        value = int(parts[1])

        if cmd == 'fd':
            dx = value * math.cos(math.radians(angle))
            dy = value * math.sin(math.radians(angle))
            x += dx
            y += dy
        elif cmd == 'lt':
            angle += value
        elif cmd == 'bk':
            dx = -value * math.cos(math.radians(angle))
            dy = -value * math.sin(math.radians(angle))
            x += dx
            y += dy
        elif cmd == 'rt':
            angle -= value

    return round(math.sqrt(x**2 + y**2))

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    test_cases = int(data[0])
    results = []

    index = 1
    for _ in range(test_cases):
        num_commands = int(data[index])
        commands = data[index + 1:index + num_commands + 1]
        index += num_commands + 1

        distance = process_commands(commands)
        results.append(distance)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()