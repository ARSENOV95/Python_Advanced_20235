import os

from ABSOLUTE_PATH import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH,'LAB_FILES','EX_2','numbers.txt')

file = open(path)

numbers =  [int(el) for el in file.read().split()]
print(numbers)