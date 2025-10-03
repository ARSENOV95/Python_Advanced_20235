import os
from ABSOLUTE_PATH_v2 import ABSOLUTE_PATH

path = os.path.join(ABSOLUTE_PATH,'text.txt')

try:
    with open(path) as file:
        print(file.readlines())
except:
    print('File not found')