import sys
from collections import deque

max_order = -sys.maxsize

food_quntity = int(input())
orders = deque(list(map(int,input().split())))


for order in orders:
    if order > max_order:
        max_order = order
#check if max order is correct
print(max_order)

curr_order = 0

while orders:
    current_order = orders.popleft()

    if current_order <=  food_quntity:
        food_quntity -= current_order
    else:
        orders.appendleft(current_order)
        break

if orders:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

else:
    print('Orders complete')
