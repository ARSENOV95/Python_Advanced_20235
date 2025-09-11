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

#loop while thare are still orders i nthe queue
while orders:
    #pop the current ortder out -- this approach since its O[1] if it's smaller than the quanity continue trough nex itteration, else beak the loop
    #the logic is wrong since the current may be > quantity, but the next might be smaller! Revise it
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
