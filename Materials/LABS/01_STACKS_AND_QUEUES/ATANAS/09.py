from collections import deque

buller_price = int(input())
barrel_size = int(input())
bullets = list(map(int,input().split()))
locks =  deque(int(x) for x in input().split())
money = int(input())

shots = 0

while locks and  bullets:

    shots +=1 
    money -= buller_price

    current_bullet = bullets.pop()

    if current_bullet <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    
    if shots == barrel_size and bullets:
        shots = 0
        print('Reloading!')

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${money}")