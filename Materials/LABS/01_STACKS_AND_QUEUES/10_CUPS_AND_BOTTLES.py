from collections import deque

cups = deque(map(int,input().split()))
bottles = list(map(int,input().split()))


wasted_water = 0

while bottles and cups:
    current_cup = cups.popleft()

    while current_cup > 0:
        current_bottle = bottles.pop()

        if current_bottle > current_cup:
            wasted_water += abs(current_cup - current_bottle)
            current_cup = 0
        else:
            current_cup  -= current_bottle

            
if not cups and bottles:
    print(f"Bottles:",*bottles)
elif cups and not bottles:
    print(f"Cups:",*cups)

print(f"Wasted litters of water: {wasted_water}")