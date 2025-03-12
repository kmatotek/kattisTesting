import math

def calculate_distance(commands):
    angle = 0.0
    x_pos = 0.0
    y_pos = 0.0
    
    for command in commands:
        direction, value = command.split()
        if direction == 'fd':
            x_pos += int(value) * math.cos(math.radians(angle))
            y_pos += int(value) * math.sin(math.radians(angle))
        elif direction == 'bk':
            x_pos -= int(value) * math.cos(math.radians(angle))
            y_pos -= int(value) * math.sin(math.radians(angle))
        elif direction == 'lt':
            angle = ((angle + int(value)) + 360) % 360
        elif direction == 'rt':
            angle = ((angle - int(value)) + 360) % 360
    
    return round(math.hypot(x_pos, y_pos))

def turtle_path():
    test_cases = int(input())
    
    for _ in range(test_cases):
        commands_num = int(input())
        commands = []
        
        for _ in range(commands_num):
            commands.append(input())
        
        print(calculate_distance(commands))


turtle_path()