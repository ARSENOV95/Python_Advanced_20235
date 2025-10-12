import os 

file = {}

parent = os.path.dirname(__file__)

for entry in os.listdir(parent):
    dir = os.path.join(parent,entry)

    if os.path.isdir(dir):
        for en in os.listdir(dir):
            sub = os.path.join(dir,en)
            if os.path.isfile(os.path.join(dir,en)):
                ext = os.path.splitext(sub)[1]
                if ext not in file.keys():
                    file[ext] = []
                file[ext].append(en)

    elif os.path.isfile(dir):
        ext1 = os.path.splitext(dir)[1]
        if ext1 not in file.keys():
            file[ext1] = []
        file[ext1].append(entry)

file = sorted(file.items())


with open(os.path.join(parent,'report.txt'),'w') as rep:
    result = ''
    for ext,file_name in file:
        result += f'{ext}\n'
        for name in file_name:
            result += f'- - - {name}\n' 

    rep.write(result)
    