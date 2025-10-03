import string

f_path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\LABS\\08_FILE_HANDLING\\FILES\\02'

output = open(f'{f_path}\\output.txt','w')

with open(f'{f_path}\\text.txt','r') as txt:

    line_n = 0

    for line in txt:
        punctuation = 0
        
        chars = 0

        for char in line:
            if char in string.punctuation:
                punctuation += 1

            elif char.isalpha():
                chars += 1
        
        line_n += 1
        output.write(f'Line {line_n} {line} ({chars})({punctuation})\n')

output.close()    
