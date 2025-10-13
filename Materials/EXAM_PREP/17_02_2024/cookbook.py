def cookbook(*args):
    dishes = {}
    result = ''

    for group in args:
        name,natianality,ingrediets = group

        if natianality not in dishes.keys():
            dishes[natianality] = []
        dishes[natianality].append((name,ingrediets))
    


    for country,recepies in sorted(dishes.items(),key = lambda x: (-len(x[1]),x[0])):
        result += f'{country} cuisine contains {len(recepies)} recipes:\n'
        for recepie in sorted(recepies):
            result += f' *{recepie[0]} -> Ingredients: {", ".join(recepie[1])}\n'

    return(result)

      
    





print(cookbook(("Spaghetti Bolognese", "Italian",["spaghetti", "tomato sauce", "ground beef"]),\
               ("Margherita Pizza", "Italian",["pizzadough", "tomato sauce", "mozzarella"]),\
               ("Tiramisu", "Italian", ["ladyfingers","mascarpone", "coffee"]),\
               ("Croissant", "French", ["flour","butter", "yeast"]),\
               ("Ratatouille", "French", ["eggplant","zucchini", "tomatoes"])))

print('##########################################')

print(cookbook(("Pad Thai", "Thai", ["rice noodles","shrimp", "peanuts", "bean sprouts", "tamarindsauce"])))

print('##########################################')
print(cookbook(("Spaghetti Bolognese", "Italian",["spaghetti", "tomato sauce", "ground beef"]),
               ("Margherita Pizza", "Italian", ["pizzadough", "tomato sauce", "mozzarella"]),
               ("Tiramisu", "Italian", ["ladyfingers","mascarpone", "coffee"]),
               ("Croissant", "French", ["flour","butter", "yeast"]),
               ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
               ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
               ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
               ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])))