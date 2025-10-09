from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque(map(int,input().split()))

total_weight = 0

while couriers and packages:
    delivered = 0
    if couriers[0] >= packages[-1]:
        new_capacity = couriers[0] - packages[-1] * 2
        if new_capacity > 0:
            couriers[0] = new_capacity
            couriers.rotate(-1)
        else:
            couriers.popleft()
        
        total_weight +=  packages.pop()
        
    else:
        packages[-1] -= couriers[0]
        total_weight += couriers.popleft()
    

print(f"Total weight: {total_weight} kg")

if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(str(x) for x in packages)}")
elif not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(str(x) for x in couriers)} but there are no more packages to deliver.")