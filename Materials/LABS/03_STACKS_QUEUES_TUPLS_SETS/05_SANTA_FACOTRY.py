crafting_materials = [int(x) for x in input().split()]
magic_lvl = [int(x) for x in input().split()]


present_level = {150:'Doll ',
                 250:'Wooden train',
                 300:'Teddy bear ',
                 400:'Bicycle '
                 }

peresents = {}

while crafting_materials and magic_lvl:
    
