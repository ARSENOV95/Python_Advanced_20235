def get_info(**kwargs): # **kwarks - packs function inpit like name = 'George', age = 20  to ['name':'George','age':20]
    return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old" #we can point the specific key from kwargs if  its in the dictinoary

print(get_info(**{"name": "George", "town":"Sofia", "age": 20}))

#get_info(**{"name": "George", "town":"Sofia", "age": 20})
#what it does is to  unpack the dictinaty into name = George, town = Sofia, age = 20 and pass it down to get_info which packs it  again to a dictionary