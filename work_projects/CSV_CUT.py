import os


f_path = 'C:\\Users\\B0060743\\Downloads\\FEZ\\'


try:
    numum_target_rows = int(input())

    input_name = input('Input file name (csv): ')
    output_file = input('Output file name (csv): ')

    input_name = (input_name + '.csv' if '.csv' not in input_name else input_name)
    output_file = (output_file + '.csv' if '.csv' not in output_file else output_file)

    with open(os.path.join(f_path,input_name),'r',encoding='UTF-8') as in_file,\
            open(os.path.join(f_path,output_file),'w',encoding= 'UTF-8') as out_file:

        rows = 0

        for row in in_file:
            if rows == numum_target_rows:
                print('Tatget lenght reached')
                break

            out_file.write(row)
            rows += 1

except ValueError:
    print('Invalid number of lines: ')