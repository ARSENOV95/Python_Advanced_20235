import os
from string import  punctuation

f_path = os.path.dirname(__file__)
in_name = 'text.txt'
out_name = 'output.txt'

with open(os.path.join(f_path,in_name),'r') as f_in,\
     open(os.path.join(f_path,out_name),'a') as f_out:
    
    for n,line in enumerate(f_in):
        punct_count = 0
        chars_count = 0

        for char in line:
            if char in punctuation:
                punct_count += 1

            elif char.isalpha():
                chars_count += 1

        f_out.write(f'Line {n + 1} {line.strip()} ({chars_count})({punct_count})\n')

 
