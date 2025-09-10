from collections import deque

customers = deque([])

while (cust_name := input()) != 'End':

    if cust_name == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(cust_name)

print(f'{len(customers)} people remaining.')

## while we  recive the command End we will
# if the custoemr name = Paid - loop trough the queue util empty and pop each customer from firsdt o last 
# else if not Paid we will append the new cuastomer as alst i nth queue 
