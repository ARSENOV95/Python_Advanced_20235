
try:
    numbers = open('D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\ADDTIONAL\\FILE_HANDLING\\numbers.txt')
except FileNotFoundError:
    print('File missing in directory')

else:
    sum_nums = 0

    for line in numbers:
        line = line.replace('\n','').strip() #removes newline simobls and strip " "

        if line.isdigit():
            digit = int(line)  #converts the number in digits
            sum_nums += digit

finally:
    numbers.close()
    exit(print(sum_nums))



