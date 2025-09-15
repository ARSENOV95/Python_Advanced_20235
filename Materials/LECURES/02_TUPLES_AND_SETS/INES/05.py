n = int(input())

parking = set(0)

for _ in range(n):
    direction, number = input().split(", ")
    if direction == 'IN':
        parking.add(number)
    elif direction == 'OUT':
        if number in parking:
            parking.remove(number)


if not parking:
    print('Parking lot is empty')
else:
    for car in parking:
        print(car)
