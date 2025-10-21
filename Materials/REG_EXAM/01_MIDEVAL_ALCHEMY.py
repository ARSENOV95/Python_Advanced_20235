from collections import deque

potions = {110: 'Brew of Immortality',
           100: 'Essence of Resilience',
           90: 'Draught of Wisdom',
           80: 'Potion of Agility',
           70: 'Elixir of Strength'
           }

crafted_options = []

substances = [int(x) for x in input().split(",")]  # LIFO
crystals = deque(int(x) for x in input().split(","))  # FIFO

while crystals and substances:
    if len(crafted_options) == 5:
        print("Success! The alchemist has forged all potions!")
        break

    curr_substance = substances[-1]
    curr_crystal = crystals[0]

    mixture = curr_substance + curr_crystal

    for amnt,potion in potions.items():
        if mixture == amnt and potion not in crafted_options:
            crafted_options.append(potion)
            substances.pop()
            crystals.popleft()
        elif (mixture >amnt):
            next_closests = [mixture - val for val in potions.keys() if mixture - val > 0 and potions[val]]
            if next_closests:

                closest = min(next_closests)
                if (mixture - closest) not in crafted_options:
                    crafted_options.append(potions[closest])

                fixed = crystals.popleft() - 20
                if fixed > 0:
                    crystals.append(fixed)
                substances.pop()
        else:
            fixed = crystals.popleft() - 5
            if fixed > 0:
                crystals.append(fixed)
            substances.pop()

        
        







if len(crafted_options) < 5:
    print("The alchemist failed to complete his quest.")

if crafted_options:
    print(f"Crafted potions: {', '.join(crafted_options)}")

substances.reverse()

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if crystals:
    print(f"Crystals: {', '.join(str(x) for x in crystals)}")

