import os

f_path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\LABS\\08_FILE_HANDLING\\FILES\\03'

while (command:= input()) != 'End':
    arguments = command.split()
    f_name = arguments[1]

    if arguments[0] == 'Create':
            with  open(f'{f_path}\\{f_name}','w') as file:
                file.write('')


