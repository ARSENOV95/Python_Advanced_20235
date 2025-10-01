import os


path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\ADDTIONAL\\FILE_HANDLING\\PROBLEM_4'


try:
    words = {} #dictinary yo howd the key words and their count


    if os.path.exists(f'{path}\\words.txt'):
        with open(f'{path}\\words.txt','r') as wds:
            
            for row in wds:
                row = row.split()
                for wod in row:
                    wod = wod.lower()
                    words[wod] = words.get(wod,0)

    if os.path.exists(f'{path}\\text.txt'):
        txt =  open(f'{path}\\text.txt','r')

except FileNotFoundError:
    print('File not on system')

else:
    import string

    output = open(f'{path}\\output.txt','w')

    for line in txt:
        for char in line.split():
            for p in string.punctuation:
                char = char.replace(p,'')
            
            char = char.lower().strip()
            if char in words.keys():
                words[char] += 1

    
    for word,count in sorted(words.items(),key = lambda x: -x[1]):
        output.write(f'{word} - {count}\n')

finally:
    exit()                
          
    


 

 


