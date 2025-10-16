from collections import deque

materails = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

toys = {150:'Doll',
        250:'Wooden train',
        300:'Teddy bear',
        400:'Bicycle'
        }

presents = {}

while materails and magic:
    curr_material = materails[-1]
    curr_magic = magic[0]

    product = curr_material * curr_magic

    if product in toys.keys():
        toy = toys[product]
        if toy not in presents.keys():
            presents[toy] = 0
        presents[toy] += 1

        materails.pop()
        magic.popleft()

    elif product < 0:
        new_val = curr_material + curr_magic

        materails.pop()
        magic.popleft()
        materails.append(new_val)
    
    elif product not in toys.keys() and product > 0:
        magic.popleft()
        materails[-1] += 15

    elif product == 0:
        if curr_material == 0:
            materails.pop()
        if curr_magic == 0:
            magic.popleft()

if ('Doll' in presents.keys() and 'Wooden train' in presents.keys()) or\
   ('Bicycle' in presents.keys() and 'Teddy bear' in presents.keys()):
    print('The presents are crafted! Merry Christmas!')

else:
    print("No presents this Christmas!")



if materails:
    materails.reverse()
    print(f"Materials left: {', '.join(str(x) for x in materails)}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic.reverse())}")

for toy,quanity in sorted(presents.items(),key = lambda x: x[0]):
    print(f'{toy}: {quanity}')
