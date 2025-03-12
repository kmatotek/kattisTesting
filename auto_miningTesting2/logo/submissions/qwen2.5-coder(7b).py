import math

def calculate_distance(commands):
    x, y = 0, 0
    angle = 0  # Initial direction: facing north (0 degrees)

    for command in commands:
        parts = command.split()
        if parts[0] == 'fd':
            distance = int(parts[1])
            x += distance * math.cos(math.radians(angle))
            y += distance * math.sin(math.radians(angle))
        elif parts[0] == 'bk':
            distance = int(parts[1])
            x -= distance * math.cos(math.radians(angle))
            y -= distance * math.sin(math.radians(angle))
        elif parts[0] == 'lt':
            angle -= int(parts[1])
        elif parts[0] == 'rt':
            angle += int(parts[1])

    # Calculate the straight-line distance from the starting point (0, 0)
    return round(math.sqrt(x**2 + y**2))

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    num_test_cases = int(data[index])
    index += 1
    
    results = []
    for _ in range(num_test_cases):
        num_commands = int(data[index])
        index += 1
        
        commands = data[index:index + num_commands]
        index += num_commands
        
        result = calculate_distance(commands)
        results.append(result)
    
    # Print all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()