expression = list(input())

opening_brackets = '{[('
closing_brackets = ')]}'

paretheses = []


for par in expression:
    if par in opening_brackets:
        paretheses.append(i)


    elif par in closing_brackets:
        if not  paretheses:
            print('NO')
            break

        elif (par == ')' and paretheses[-1] == '(') or\
           (par == ']' and paretheses[-1] == '[') or\
           (par == '}' and paretheses[-1] == '{'):        
            paretheses.pop()
        

if not paretheses:
    print('YES')
else:
    print('NO')
