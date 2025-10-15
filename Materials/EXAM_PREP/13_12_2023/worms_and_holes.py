from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())


matches  = 0

while worms and holes:
    curr_hole = holes[0]
    curr_worm = worms[-1]

    if curr_worm == curr_hole:
        matches  += 1
        holes.popleft()
        worms.pop()
    else:
        worms[-1] -=3
        if  worms[-1] <= 0:
            worms.pop()
        holes.popleft()
    



if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms:
    print("Every worm found a suitable hole!")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes: 
    print("Holes left: none")
elif holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")


