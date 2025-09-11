expression = list(input())

opening_brackets = '{[('
closing_brackets = ')]}'

paretheses = []


for i in expression:
    if i in opening_brackets:
        paretheses.append(i)
    elif i in closing_brackets:
        if (i == ')' and paretheses[-1] == '(') or\
           (i == ']' and paretheses[-1] == '[') or\
           (i == '}' and paretheses[-1] == '{'):
                     
            paretheses.pop()
        else:
            break

if not paretheses:
    print('YES')
else:
    print('NO')
