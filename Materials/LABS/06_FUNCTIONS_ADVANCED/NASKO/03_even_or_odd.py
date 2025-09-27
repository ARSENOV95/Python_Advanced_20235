def even_odd(*args):
    command = args[-1]
    if command == 'even':
        return [x for x in args if x %2 == 0]
    return [x for x in args if x %2 != 0] 
    