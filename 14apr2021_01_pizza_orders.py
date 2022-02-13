from collections import deque

pizza_orders = deque([int(el) for el in input().split(', ') if 0 < int(el) <= 10])
employees = [int(el) for el in input().split(', ')]

total_pizza_made = 0
while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    current_employee = employees.pop()
    if current_order > current_employee:
        current_order -= current_employee
        total_pizza_made += current_employee
        pizza_orders.appendleft(current_order)
    else:
        total_pizza_made += current_order

if pizza_orders:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(el) for el in pizza_orders)}')
elif employees:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print(f'Employees: {", ".join(str(el) for el in employees)}')