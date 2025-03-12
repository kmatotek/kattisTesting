def calculate_min_exchange(trip_expenses):
    total_cost = sum(trip_expenses)
    average_cost = total_cost / len(trip_expenses)
    exchange_total = 0
    
    for cost in trip_expenses:
        exchange_total += (cost - average_cost) * 100
    
    return round(abs(exchange_total) / 100, 2)

def process_input():
    while True:
        n = int(input())
        if n == 0:
            break
        trip_expenses = []
        for _ in range(n):
            expense = float(input())
            trip_expenses.append(expense)
        min_exchange = calculate_min_exchange(trip_expenses)
        print(f'${min_exchange:.2f}')

process_input()