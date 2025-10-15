from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())


matches  = 0

while worms and holes:
    curr_hole = holes.popleft()
    curr_worm = worms.pop()

    if curr_worm == curr_hole:
        matches  += 1

    else:
        curr_worm -= 3
        if curr_worm > 0:
            if curr_worm == curr_hole:
                matches  += 1
       





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


