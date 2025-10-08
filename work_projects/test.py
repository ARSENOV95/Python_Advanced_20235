import os

clean_simbols = (',')

f_path = 'C:\\Users\\B0060743\\Downloads\\FEZ\\'
file = input('csv: ')

path = os.path.join(f_path,file)

try:
    with open(path,'r') as file:
        for _ in file:
            print(file.readlines())

    

except FileNotFoundError:
    print('Missing')