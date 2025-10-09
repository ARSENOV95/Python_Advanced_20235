import os 
import re

from ABSOLUTE_PATH import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH,'lab_files','EX_5')

with open(os.path.join(path,'input.txt')) as file:
    text = file.read()


with  open(os.path.join(path,'words.txt')) as file:
    words = file.read().split()


data = {}

for word in words: #for every word in the file with words
    pattern = rf'\b{word}\b'  #f - marks that the word is dinamic #a patter which looks for the exact word - with bounderies  F is format for thw ord to be dynamic like f String
    count = len(re.findall(pattern,text)) #count is a varaible to store the count of all elements from the text that match the apttern (in its original form a list with matches)
    data[word] = count #finally we add the count ot the dictionary 

sorted_data = sorted(data.items(), key = lambda kvp: -kvp[1])

with open(os.path.join(path,'output.txt'),'w') as file:
    for key,value in sorted_data:
        file.write(f'{key} - {value}')