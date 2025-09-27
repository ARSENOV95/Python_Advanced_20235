def get_info(**info):
    name,town,age = [y for y in info.values()]
    return f'This is {name} from {town} and he is {age} years old'


print(get_info(**{"name": "George", "town":"Sofia", "age": 20}))