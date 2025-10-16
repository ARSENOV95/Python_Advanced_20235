def accommodate_new_pets(capacity :int,max_weight :float,*args):
    accomuadated = {}
    result = []

    for pet,weight in args:
        if capacity == 0:
            result.append('You did not manage to accommodate all pets!')
            break

        if weight > max_weight:
            continue

        if pet not in accomuadated.keys():
            accomuadated[pet] = 0
        accomuadated[pet] += 1
        capacity -= 1
    
    if capacity:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.")
    
    result.append("Accommodated pets:")

    for pet,count in sorted(accomuadated.items()):
        result.append(f'{pet}: {count}')
    
    return '\n'.join(result)
        

print(accommodate_new_pets( 
    10, 
    15.0, 
    ("cat", 5.8), 
    ("dog", 10.0), 
))


print(accommodate_new_pets( 
    10, 
    10.0, 
    ("cat", 5.8), 
    ("dog", 10.5), 
    ("parrot", 0.8), 
    ("cat", 3.1), 
))

print(accommodate_new_pets( 

    2, 

    15.0, 

    ("dog", 10.0), 

    ("cat", 5.8), 

    ("cat", 2.7), 

)) 