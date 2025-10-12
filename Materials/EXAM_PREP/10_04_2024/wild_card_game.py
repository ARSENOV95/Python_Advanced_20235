def draw_cards(*args,**kwargs):
    monsters = set()
    spells = set()
    result  = ''

    spells.update([f'  $$${name}' for name,type in args if type == 'spell'])
    monsters.update([f'  ***{name}' for name,type in args if type == 'monster'])

    spells.update([f'  $$${key}' for key,val in kwargs.items() if val == 'spell'])
    monsters.update([f'  ***{key}' for key,val in kwargs.items() if val == 'monster'])

    spells_lst = list(spells)
    monsters_lst = list(monsters)


    if monsters_lst:
        result += 'Monster cards:\n'
        for monster in sorted(monsters_lst,reverse= True):
            result += f'{monster}\n'

    if spells_lst:
        result += 'Spell cards:\n'
        for spell in sorted(spells_lst):
            result += f'{spell}\n'
    return result


print(draw_cards(("cyber dragon","monster"), freeze="spell",))

#print(draw_cards(("brave attack","spell"), ("freeze", "spell"),lightning_bolt="spell",fireball="spell",))