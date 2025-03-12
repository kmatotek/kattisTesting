def calculate_minimum_exchange():
    while True:
        n = int(input())
        if n == 0:
            break

        expenses = []
        for _ in range(n):
            expenses.append(float(input()))

        average = sum(expenses) / n
        above_average = [x for x in expenses if x > average]
        below_average = [x for x in expenses if x < average]

        exchange = sum(above_average) - len(above_average) * average
        exchange = round(exchange, 2)

        print(f'${exchange:.2f}')

calculate_minimum_exchange()