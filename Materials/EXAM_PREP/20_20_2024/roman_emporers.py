def list_roman_emperors (*args,**kwargs):
    success = {}
    fail = {}
    for arg in args:
        name,status = arg
        if name in kwargs.keys():
            if status == True:
                success[name] = kwargs[name]
            elif status == False:
                fail[name] = kwargs[name]



    result = f"Total number of emperors: {len(success) + len(fail)}\n"

    if success:
       result += 'Successful emperors:\n' # the next conatinted val wll be on a new row
       success = sorted(success.items(),key = lambda x: (-x[1],x[0]))
     
       result += '\n'.join(f'****{name}: {years}' for name,years in success)   #\n is used as a join between the values of the comprehension the first vall will not have it

    if fail:
        result += '\nUnsuccessful emperors:\n' # the next conatinted val wll be on a new row
        fail = sorted(fail.items(),key = lambda x: (x[1],x[0]))

        result += '\n'.join(f'****{name}: {years}' for name,years in fail)
    
    return result


#print(list_roman_emperors(("Augustus", True),("Nero", False),Augustus=40, Nero=14,))
#print(list_roman_emperors(("Augustus", True),("Trajan", True), ("Nero",False), ("Caligula",False), ("Pertinax",False), ("Vespasian",True), Augustus=40,Trajan=19, Nero=14,Caligula=4, Pertinax=4,Vespasian=19,))

#print(list_roman_emperors(("Augustus", True),("Trajan", True),("Claudius", True),Augustus=40, Trajan=19,Claudius=13,))