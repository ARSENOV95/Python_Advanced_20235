import os

from ABSOLUTE_PATH import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH,"LAB_FILES","EX_3","my_first_file.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print('File already deleted')