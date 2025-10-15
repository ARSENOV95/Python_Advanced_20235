from collections import deque

monster_armour = deque(map(int,input().split(',')))
soldier_strikes = [int(x) for x in input().split(',')]

killed_monsters = 0

while monster_armour and soldier_strikes:
    curr_strike = soldier_strikes.pop()
    curr_monster = monster_armour.popleft()
    
    if curr_strike >= curr_monster:
        curr_strike -= curr_monster
        
        if curr_strike > 0:
            if len(soldier_strikes) == 1:
                soldier_strikes.append(curr_strike)
            elif len(soldier_strikes) > 1:
                soldier_strikes[-1] += curr_strike
        killed_monsters += 1
    
    else:
        curr_monster -= curr_strike
        monster_armour.append(curr_monster)
        


if not monster_armour and soldier_strikes:
    print("All monsters have been killed!")
if not soldier_strikes and monster_armour:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")


