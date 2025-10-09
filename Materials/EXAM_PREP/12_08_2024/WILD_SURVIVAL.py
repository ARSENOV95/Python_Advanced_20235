BEE_KILLS_PER_EATER = 7
from collections import deque

bees = deque(map(int,input().split()))
bee_eaters = [int(x) for x in input().split()]

while bees and bee_eaters:    
    bee_group  = bees[0]
    eater_group = bee_eaters[-1]

    battle = round(bee_group / BEE_KILLS_PER_EATER)

    if eater_group - battle > 0:
        bee_eaters[-1] -= battle
        bees.popleft()
        

    elif eater_group - battle == 0:
        bees.popleft()
        bee_eaters.pop()

    elif eater_group - battle < 0:
        bees.popleft()
        bee_eaters.pop()
        bees.append(abs(eater_group - battle) * BEE_KILLS_PER_EATER) 
        
        

print('The final battle is over!')

if bees:
    print(f'Bee groups left: {", ".join(str(x) for x in bees)}')
elif bee_eaters:
    print(f'Bee-eater groups left: {", ".join(str(x) for x in bee_eaters)}')
else:
    print("But no one made it out alive!")


