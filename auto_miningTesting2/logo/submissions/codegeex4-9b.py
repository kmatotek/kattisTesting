import math

class Turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0

    def forward(self, distance):
        self.x += distance * math.cos(math.radians(self.angle))
        self.y += distance * math.sin(math.radians(self.angle))

    def backward(self, distance):
        self.x -= distance * math.cos(math.radians(self.angle))
        self.y -= distance * math.sin(math.radians(self.angle))

    def turn_left(self, degree):
        self.angle += degree

    def turn_right(self, degree):
        self.angle -= degree


def calculate_distance(turtle):
    return round(math.sqrt(turtle.x**2 + turtle.y**2))


def process_commands(commands):
    turtle = Turtle()
    for command in commands:
        parts = command.split()
        action = parts[0]
        value = int(parts[1])
        if action == "fd":
            turtle.forward(value)
        elif action == "bk":
            turtle.backward(value)
        elif action == "lt":
            turtle.turn_left(value)
        elif action == "rt":
            turtle.turn_right(value)
    return calculate_distance(turtle)


def main():
    num_test_cases = int(input())
    results = []
    for _ in range(num_test_cases):
        num_commands = int(input())
        commands = [input().strip() for _ in range(num_commands)]
        distance = process_commands(commands)
        results.append(distance)
    
    for result in results:
        print(result)


if __name__ == "__main__":
    main()