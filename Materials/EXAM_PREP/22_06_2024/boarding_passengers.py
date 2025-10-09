def boarding_passengers(capacity :int,*args):
    guest_list = {}
    result = 'Boarding details by benefit plan:\n'
    groups = set()

    for occupents,group in args:
        groups.add(group)

        if occupents <= capacity:    
            if group not in guest_list.keys():
                guest_list[group] = 0
            guest_list[group] += occupents
            capacity -= occupents
   
    
    guest_list = sorted(guest_list.items(),key = lambda x: (-x[1],x[0]))

    result += '\n'.join(f'## {guests}: {passangers} guests' for guests,passangers in guest_list)
    
    if len(guest_list) ==  len(set(args)):
       result += '\nAll passengers are successfully boarded!'
    elif capacity == 0:
        result += '\nBoarding unsuccessful. Cruise ship at full capacity.'
    else:
        result += f'\nPartial boarding completed. Available capacity: {capacity}.'

    return result

#print(boarding_passengers(150, (35,'Diamond'), (55, 'Platinum'), (35,'Gold'), (25, 'First Cruiser')))
#print(boarding_passengers(100, (20,'Diamond'), (15, 'Platinum'),(25,'Gold'), (25, 'First Cruiser'), (15,'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30,'Gold'), (20, 'Platinum'), (30,'Diamond'), (10, 'First Cruiser'), (31,'Platinum'), (20, 'Diamond')))
