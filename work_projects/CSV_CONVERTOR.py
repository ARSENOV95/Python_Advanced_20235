import os


input_name = ''

while input_name == '':
    try:
        clean_simbols = set() # to avoid dulicates

        #add avalidation if blank 
        while  True:
            print('Please enter a symbol to rpelace ot  DONE if done: ')
            symbol = input('Insert symbol to clean: ')

            if symbol.upper() == 'DONE':
                break

            replace = input('Please enter a symbol to replace with: ')
            clean_simbols.add((symbol,replace))


    
        #file dir and name, need to add a validation function
        f_path = 'C:\\Users\\B0060743\\Downloads\\FEZ\\'
        input_name = input('Input file name (csv): ')
        output_file = input('Output file name (csv): ')


        input_name = (input_name + '.csv' if '.csv' not in input_name else input_name)
        output_file = (output_file + '.csv' if '.csv' not in output_file else output_file)

        with open(os.path.join(f_path,input_name),'r',encoding='UTF-8') as in_file,\
            open(os.path.join(f_path,output_file),'w',encoding= 'UTF-8') as out_file:
            for line in in_file:
                for symbol,replace in clean_simbols:
                    if symbol in line:
                        line = line.replace(symbol,replace)
                out_file.write(line)
            
    except FileNotFoundError:
        print('File not found')
        continue

