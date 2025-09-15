car_flow = int(input())

car_lot = set()

for car in range(car_flow):
    action,number = input().split(", ")

    if action == 'IN':
        car_lot.add(number)
    else:
        action == 'OUT'
        car_lot.discard(number)

if car_lot:
    print(*car_lot, sep='\n')

else:
    print('Parking Lot is Empty')
