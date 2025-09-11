from collections import deque

quantity_of_food = int(input())

orders  = deque(int(x) for x in input().split()) # we can use a coprehension as imput for a deque and it will create a list

print(max(orders))

#twho criteria to end the loop if the list is empty and the first order is > than the quantity
#basically [0] will laways be the first order
while orders and orders[0] <= quantity_of_food:
    quantity_of_food -= orders.popleft()

if orders:
    print('Orders left: ' + f"{*orders, },sep=', '")
else:
    print('Orders complete')