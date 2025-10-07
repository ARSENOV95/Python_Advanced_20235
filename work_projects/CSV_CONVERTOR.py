import os

clean_simbols = ('"',' ')

f_path = 'C:\\Users\\B0060743\\Downloads\\FEZ\\'



input_name = ''

while input_name == '':
    try:
        input_name = input('Input file name (csv): ')
        output_file = input('Output file name (csv): ')

        input_name = (input_name + '.csv' if '.csv' not in input_name else input_name)
        output_file = (output_file + '.csv' if '.csv' not in output_file else output_file)

        with open(os.path.join(f_path,input_name),'r',encoding='UTF-8') as in_file,\
            open(os.path.join(f_path,output_file),'w',encoding= 'UTF-8') as out_file:
            for line in in_file:
                for symbol in clean_simbols:
                    if symbol in line:
                        line = line.replace(symbol,'')
                out_file.write(line)
            
    except FileNotFoundError:
        print('File not found')
        continue

