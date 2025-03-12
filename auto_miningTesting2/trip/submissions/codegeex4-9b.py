def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        expenses = []
        for _ in range(n):
            expense = float(input())
            expenses.append(expense)
        
        total_expenses = sum(expenses)
        average_expense = total_expenses / n
        rounding_diff = round(average_expense) - average_expense
        
        exchange_amounts = [round((expense - average_expense + rounding_diff), 2) for expense in expenses]
        total_exchange = round(sum(exchange_amounts), 2)
        
        print(f'${total_exchange:.2f}')

if __name__ == "__main__":
    main()