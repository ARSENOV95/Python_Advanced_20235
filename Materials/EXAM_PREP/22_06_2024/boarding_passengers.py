def boarding_passengers(capacity :int,*args):
    total_guests = sum(group[0] for group in args)
    guest_list = {}

    for occupents,group in args:

        if occupents <= capacity:    
            if group not in guest_list.keys():
                guest_list[group] = 0
            guest_list[group] += occupents
            capacity -= occupents
        
        if capacity == 0:
            break

    onboarded = sum(val for val in guest_list.values()) 

    guest_list = sorted(guest_list.items(),key = lambda x: (-x[1],x[0]))

    result = 'Boarding details by benefit plan:\n'
    for guests,passangers in guest_list:
        result += f'## {guests}: {passangers} guests\n' 
    #notes : be careful where you put the new line
    if onboarded ==  total_guests:
       result += 'All passengers are successfully boarded!'
    
    elif capacity == 0:
        result += 'Boarding unsuccessful. Cruise ship at full capacity.'
        
    elif capacity != 0 and onboarded !=  total_guests:
        result += f'Partial boarding completed. Available capacity: {capacity}.'

    return result

#print(boarding_passengers(150, (35,'Diamond'), (55, 'Platinum'), (35,'Gold'), (25, 'First Cruiser')))
#print(boarding_passengers(100, (20,'Diamond'), (15, 'Platinum'),(25,'Gold'), (25, 'First Cruiser'), (15,'Diamond'), (10, 'Gold')))
#print(boarding_passengers(120, (30,'Gold'), (20, 'Platinum'), (30,'Diamond'), (10, 'First Cruiser'), (31,'Platinum'), (20, 'Diamond')))
