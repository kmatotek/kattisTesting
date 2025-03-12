while True:
    n = int(input())
    
    if not n: break
    
    students_expenses = [float(input()) for _ in range(n)]
    total_expense = sum(students_expenses)
    
    equal_share_per_student = total_expense / n
    
    exchange_amounts = []
    remaining_debt = 0.00
    
    for i in range(n):
        difference = students_expenses[i] - equal_share_per_student
        
        if difference > 0:
            exchange_amounts.append(difference)
            
            remaining_debt += difference
        elif difference < 0:
            exchange_amounts.append(0.00)
    
    # Since the total amount of money to be exchanged must be zero,
    # the last student should not receive any money.
    for i in range(n):
        if exchange_amounts[i] == remaining_debt:
            exchange_amounts.pop(i)
            break
    
    min_total_exchange = sum(exchange_amounts)
    
    print(f'${min_total_exchange:.2f}')