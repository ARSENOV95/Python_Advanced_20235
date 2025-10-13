def plant_garden(plot_sapce :int,*plant_space,**plants):
    total_space = plot_sapce

    planted_plants = {}

    result = ''

    for plant,space in plant_space:
        if plant in plants.keys():
            planted = plants[plant] * space

            if planted <= total_space:
                planted_plants[plant] = plants[plant]
                total_space -= planted
            else:
                planted_plants[plant] = int(total_space//space)
                total_space -= int(total_space//space)
        if total_space == 0:
            break

        planted_plants[plant] = planted

        
    if total_space:
        result += f'All plants were planted! Available garden space: {total_space} sq meters.\nPlanted plants:\n'
    else:
        result += 'Not enough space to plant all requested plants!\nPlanted plants:\n'


    planted_plants = sorted(planted_plants.items(),key = lambda x: x[0])
    
    for type_pl,quan in planted_plants:
        if quan > 0:
            result += f'{type_pl}: {quan}\n'

    return result
                


#print(plant_garden(50.0, ("rose",2.5), ("tulip", 1.2), ("sunflower",3.0), rose=10, tulip=20)) 
#print(plant_garden(20.0, ("rose",2.0), ("tulip", 1.2), ("sunflower",3.0), rose=10, tulip=20,sunflower=5)) 
print(plant_garden(2.0, ("rose",2.5), ("tulip", 1.2), ("daisy",0.2), rose=4, tulip=15, sunflower=3,daisy=4)) 
#print(plant_garden(50.0, ("tulip",1.2), ("sunflower", 3.0), rose=10,tulip=20, daisy=1))