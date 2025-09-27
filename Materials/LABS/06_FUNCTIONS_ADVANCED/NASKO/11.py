def math_operations(*args,**kwargs):
    for i in range(len(args)):
        if i % 4 == 0:
            kwargs['a'] += args[i] 
        elif i % 4 == 1:
            kwargs['s'] -= args[i] 
        elif i % 4 == 2:
            if args[i] > 0:
                kwargs['d'] /= args[i]     
        elif i % 4 == 3: 
            kwargs['m'] *= args[i]     

    kwargs = sorted(kwargs.items(), key = lambda x: (-x[1],x[0]))

    result = []

    return '\n'.join(f'{key}: {val:.1f}' for key,val in kwargs)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7,d=33, m=15))