import os
from ABSOLUTE_PATH import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH,"LAB_FILES","EX_3","my_first_file.txt")

with open(path,'w') as file:
    file.write('I just created my first file!')