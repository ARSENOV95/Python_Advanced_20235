import os

f_path = 'D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\LABS\\08_FILE_HANDLING\\FILES\\03'

while (command:= input()) != 'End':
    arguments = command.split("-")
    f_name = arguments[1]

    if arguments[0] == 'Create':
        file = open(f'{f_path}\\{f_name}','w') 
        file.close()

    elif arguments[0] == 'Add':
        content = arguments[2]
        try:
            file = open(f'{f_path}\\{f_name}','a') 
            file.write(f"{content}\n")
        except FileNotFoundError:
            ile = open(f'{f_path}\\{f_name}','w') 
            file.write(f"{content}\n")
    elif arguments[0] == 'Replace':
        old_string,new_string = arguments[2:]
        try:
      




 

