from math import log

def logg(num :int,base):
    if base == 'natural':
        return f'{log(num):.2f}'
    elif base.isdigit():
        return f'{log(num,float(base)):.2f}'


number = int(input())
l_base = input() #ig natural it will be an exponent e^n


print(logg(number,l_base))