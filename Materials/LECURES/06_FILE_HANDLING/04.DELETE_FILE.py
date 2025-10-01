import os

f_path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\ADDTIONAL\\FILE_HANDLING\\my_first_file.txt'

try:
    os.remove(f_path)
except FileNotFoundError:
    print('File missing')

finally:
    exit()

