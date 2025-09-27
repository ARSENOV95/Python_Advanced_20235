def even_odd_filter(**kwargs):
    for key,num_list in kwargs.items():
        if key == "even":
            kwargs[key] = [x for x in num_list if x % 2 == 0]
        else:
            kwargs[key] = [x for x in num_list if x % 2 != 0]

    return dict(sorted(kwargs.items(),key = lambda x: -len(x[1]))) #cast each key:value tuple as  a key-value pair