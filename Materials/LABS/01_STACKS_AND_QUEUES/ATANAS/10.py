from collections import deque

cups = deque(map(int,input().split()))
bottles = list(map(int,input().split()))

wasted_water = 0 

while bottles and cups:
    current_cup = cups[0]

    while current_cup > 0 and bottles:
        bottle = bottles.pop()

        if bottle > current_cup:
            wasted_water +=  bottle - current_cup
            current_cup = 0
        else:
            current_cup  -= bottle
    if current_cup <= 0:
        cups.popleft()
    else:
        break

            
if not cups and bottles:
    print(f"Bottles:",*bottles[::-1])
elif cups and not bottles:
    print(f"Cups:",*cups)

print(f"Wasted litters of water: {wasted_water}")