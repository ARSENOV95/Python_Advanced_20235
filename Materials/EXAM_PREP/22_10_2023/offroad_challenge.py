from collections import deque

initial_fuel = list(map(int,input().split()))
consumption_indexes = deque(map(int,input().split()))
quantities_needed = deque(map(int,input().split()))

stops = 1
reached_altitudes = []

while initial_fuel and consumption_indexes and quantities_needed:
    total_consuption = initial_fuel[-1] - consumption_indexes[0]
    
    if total_consuption < quantities_needed[0]:
        print(f"John did not reach: Altitude {stops}")
        break

    if total_consuption >= consumption_indexes[0]:
        print(f"John has reached: Altitude {stops}")
        reached_altitudes.append(f'Altitude {stops}')
        initial_fuel.pop()
        consumption_indexes.popleft()
        quantities_needed.popleft()

    stops += 1
    
if not quantities_needed:
    print("John has reached all the altitudes and managed to reach the top!")
elif quantities_needed:
    print("John failed to reach the top.")
    if not reached_altitudes:
        print("John didn't reach any altitude.")
    else:
        print(f"Reached altitudes: {', '.join(reached_altitudes)}")
