def even_odd(*args):
    command,nums = args[-1],args[:-1]
    if command == 'even': #based o nthe condtion the last element =  command
        return  list(filter(lambda x: x %2 == 0,nums)) #takes elements - 1 fromn the tuple = the numebrs only 
    return  list(filter(lambda x: x % 2 != 0,nums))

#print(even_odd(1, 2, 3, 4, 5, 6, "even")) #test code
