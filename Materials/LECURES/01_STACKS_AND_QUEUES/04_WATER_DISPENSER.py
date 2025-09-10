from collections import deque

liters = int(input())

people = deque([])

while (name:= input()) != 'Start':
    people.append(name)

while (command := input()) != 'End':
    if command.isnumeric():
        if int(command) <= liters:
            print(f'{people[0]} got water')
            liters -= int(command)
        else:
            print(f"{people[0]} must wait")
        
        people.popleft()

    elif command.startswith('refill'):
        _,refuel_liters = command.split()
        refuel_liters = int(refuel_liters)

        liters += refuel_liters

print(f'{liters} liters left')