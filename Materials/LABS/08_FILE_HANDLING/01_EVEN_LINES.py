import os

REPLACEMENT = '@'
specails = ("-", ",", ".", "!", "?")

f_path = os.path.dirname(__file__)
f_name = 'text.txt'

with open(os.path.join(f_path,f_name),'r') as f:
    readble  = f.read().split('\n')

    for line_n,line in enumerate(readble):
        if line_n %2 == 0:
            for char in specails:
                line = line.replace(char,REPLACEMENT)
            print(" ".join(reversed(line.split())))

    


            












