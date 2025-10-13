def plant_garden(space,*allowed_plants,**requests):
    sorted_requests = sorted(requests.items(),key = lambda x:x[0])
    plants_planted = []

    all_planted = True

    for plant,quanitity in sorted_requests:
        for p,s in allowed_plants:
            if plant == p:
                planted = min(quanitity,int(space//s))
                if planted < quanitity:
                    all_planted = False
                if planted > 0:
                    plants_planted.append((plant,planted))
                    space -= planted * s
                break


    result = []
    if all_planted:
        result.append(f"All plants were planted! Available garden space: {space:.2f} sq meters.")
    else:
        result.append(f"Not enough space to plant all requested plants!")

    result.append("Planted plants:")
    for plant,quanitity in plants_planted:
        result.append(f"{plant}: {quanitity}")

    return "\n".join(result)


print(plant_garden(50.0, ("rose",2.5), ("tulip", 1.2), ("sunflower",3.0), rose=10, tulip=20))