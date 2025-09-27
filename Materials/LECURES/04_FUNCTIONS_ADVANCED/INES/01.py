def multiply(*args):
    result = 1 #we need to have a value for 1 to start with as it cant be none * integer
    for el in args: #we treat args like a normal tuple
        result *= el #we multiply each evelemnt of the tuple, we start with 1  * the first element
    return result

#whene multiply(a, b = 0 *args):
# is is mandatory parameter, so we need to define it as an argument when we call the function