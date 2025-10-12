import os

ERR = "An error occurred"


path = os.path.dirname(__file__) #sets a dinamic path  = the current working dirtoory


while (command:= input()) != 'End':  #decided to use a wallrous operator as  i did not use ti for a while 
    args = command.split("-")
    action,f_name = args[:2]



    if action == 'Create':
        with open(os.path.join(path,f_name),'w') as file:
            file.write('')

    elif action == 'Add':      
        content  =args[2]
        with open(os.path.join(path,f_name),'a') as file:    
            file.write(f'{content}\n')
        
    
    elif action == 'Replace':
        old_string,new_string = args[2:]

        try:
            with open(os.path.join(path,f_name),'r+') as file_r:
                reader = file_r.read()
                data = reader.replace(old_string,new_string)

            with open (os.path.join(path,f_name),'w') as file_w:
                file_w.write(data)

        except:
            print(ERR)
            continue

    elif action == 'Delete':
        try:
            os.remove(os.path.join(path,f_name))
        except:
            print(ERR)
            continue
