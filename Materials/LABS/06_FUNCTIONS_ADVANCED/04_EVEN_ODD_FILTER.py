def even_odd_filter(**kwargs):
    sorted_dict = {}
    for key,vals in kwargs.items():
            if key == 'even':
                kwargs[key] = list(filter(lambda x:x % 2 == 0,vals))
            else:
                kwargs[key] = list(filter(lambda x:x % 2 != 0,vals))

    for  key,value in sorted(kwargs.items(),key = lambda x: -len(x[1])): # we have to loop trough the sorted tuple pairs after sorting and append them ro a new dicitoanry
         sorted_dict[key] = value

    return sorted_dict


#print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5],even=[3, 4, 5, 7, 10, 2, 5, 5, 2],)) - testmputn