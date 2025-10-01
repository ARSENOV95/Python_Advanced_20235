

try:
    open('D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\ADDTIONAL\\FILE_HANDLING\\text.txt') #opens the file and prints File found
    #\ must be used to escape the \ simobles i nthe absolute path
    print('File found')
except FileNotFoundError:
    print('File not found')
finally:
    exit()

