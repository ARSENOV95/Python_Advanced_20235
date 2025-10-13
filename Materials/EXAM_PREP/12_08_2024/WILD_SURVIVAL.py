from math import ceil
KILLS_PER_EATER = 7

from collections import deque

bees = deque(int(el) for el in input().split())
bee_eaters = [int(el) for el in input().split()]

while bees and bee_eaters:
    bees_group = bees[0]
    eater_group = bee_eaters[-1]

    attack  = (eater_group * KILLS_PER_EATER) - bees_group #reaults the amoutn of eaters survived 
    #print(attack)
    if attack > 0: #if there are alvie aters we the colosest biggest round number
        bee_eaters[-1] = ceil(attack/KILLS_PER_EATER)
        bees.popleft()

    elif attack < 0:
        bees[0] = abs(attack)
        bee_eaters.pop()
        bees.rotate(-1)
    else:
        bee_eaters.pop()
        bees.popleft()
    
    #print(bees)
    #print(bee_eaters)

print('The final battle is over!')

if (bees and not bee_eaters) or (bee_eaters and not bees):
    if bees:
        print(f"Bee groups left: {', '.join(str(el) for el in bees)}")
    if bee_eaters:
        print(f"Bee-eater groups left: {', '.join(str(el) for el in bee_eaters)}")
else:
    print('But no one made it out alive!')
    


