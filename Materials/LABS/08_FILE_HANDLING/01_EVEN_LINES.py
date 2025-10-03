import os

from collections import deque

def formatter(line):
    specials = ("-", ",", ".", "!", "?")
    sorted = deque([])

    for word in line:
        for p in specials:
            if p in word:
                word = word.replace(p,'@')

        sorted.appendleft(word)
    
    return sorted

f_path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\LABS\\08_FILE_HANDLING\\FILES\\01'


try:
    if os.path.exists(f'{f_path}\\text.txt'):
        text = open(f'{f_path}\\text.txt','r')

except FileNotFoundError:

    text = open(f'{f_path}\\text.txt','w')
    text.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n-Quick, hide here. It is safer.")

else:
    formatted = [line.split() for line in text]
    
    for i in range(len(formatted)):
        if i %2 == 0:
            formatted[i] = formatter(formatted[i])
            print(*formatted[i])

finally:
    text.close()
 
            












