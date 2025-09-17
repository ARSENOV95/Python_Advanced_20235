from collections import deque

working_bees = deque(map(int,input().split()))
nectar = list(map(int,input().split()))
symbols = deque(input().split())

oper = {"+": lambda a,b: a + b,
              "*": lambda a,b: a * b,
              "-": lambda a,b: a - b,
              "/": lambda a,b: a / b if b != 0 else 0,         
            }

total_honey = 0

while working_bees and nectar:
   

    if nectar[-1] >= working_bees[0]:
        curr_bee = working_bees[0]
        curr_necatar = nectar[-1]
        oepration = symbols[0]
        
        total_honey += abs(oper[oepration](curr_bee,curr_necatar))
        curr_bee = working_bees.popleft()
        curr_necatar = nectar.pop()
        oepration = symbols.popleft()
    else:
        if nectar[-1] <  working_bees[0]:
            nectar.pop()
            continue
        
print(f'Total honey made: {total_honey}')

if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')

if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')