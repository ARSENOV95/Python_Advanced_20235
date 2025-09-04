from collections import deque

liters = int(input())

people = deque([])

while (command:=  input()) != "Start":
    people.append(command)

while (command:=  input()) != "End":
    if command.isnumeric() and int(command) <= liters:
        print(f'{people.popleft()} got water')
        liters -=  int(command)

    elif command.startswith("refill"):
        _ , liters_to_refill = command.split()
        liters_to_refill = int(liters)
        liters += liters_to_refill
        
    else:
        print(f'{people.popleft()} must wait')

print(f'{liters} liters left')





