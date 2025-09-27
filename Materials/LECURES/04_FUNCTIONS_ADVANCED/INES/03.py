def bla(name,age):
    return name,age

test = {'name':'Asen','age':30}

print(bla(**test))