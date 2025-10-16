from collections import deque

crafting_materials = [int(x) for x in input().split()]
magic_lvl = deque(int(x) for x in input().split())


present_level = {150:'Doll',
                 250:'Wooden train',
                 300:'Teddy bear ',
                 400:'Bicycle '
                 }

peresents = {}

while crafting_materials and magic_lvl:
    curr_box = crafting_materials[-1]
    curr_magic = magic_lvl[0]
    
    toy = curr_box * curr_magic

    if toy in present_level.keys():
        if present_level[toy] not in  peresents.keys():
            peresents[present_level[toy]] = 0
        peresents[present_level[toy]] += 1

        crafting_materials.pop()
        magic_lvl.popleft()

    elif toy not in present_level and toy > 0:
        magic_lvl.popleft()
        crafting_materials[-1] += 15

    elif curr_magic == 0 or curr_box == 0:
        if curr_magic == 0:
            magic_lvl.popleft()
        elif curr_box == 0:
             crafting_materials.pop()
        elif sum(curr_magic,crafting_materials) == 0:
            crafting_materials.pop()
            magic_lvl.popleft()

