from functools import reduce
def operate(operator,*args):
    if operator == '+':
        return reduce(lambda x,y: x + y,args) # performs an action an element  if we have a  + and tuple (1,2,3) i it will work like 1+2,3  ->3 + 3 = 6 and will stop
    elif operator == '-':
        return reduce(lambda x,y: x - y,args)
    elif operator == '*':
        return reduce(lambda x,y: x * y,args)
    elif operator == '/':
        return reduce(lambda x,y: x / y,args) #this will print erro whnethere are nulls
    
