from collections import deque

cups = deque(map(int,input().split()))
bottles = list(map(int,input().split()))

wasted_water = 0 

while cups and bottles:
    current_cup = cups[0]

    while  current_cup > 0 and bottles:
        current_bottle = bottles.pop()
        current_cup -= current_bottle
    wasted_water -= current_cup
    cups.popleft()

if not cups and bottles:
    print(f"Bottles:",*bottles)
elif cups and not bottles:
    print(f"Cups:",*cups)

print(f"Wasted litters of water: {wasted_water}")