
try:
    numbers = open('D:\\Files\\SOFT_UNI\\Python_Advanced_20235\\Materials\\ADDTIONAL\\FILE_HANDLING\\numbers.txt')
except FileNotFoundError:
    print('File missing in directory')

else:
    sum_nums = 0

    for line in numbers:
        line = line.replace('\n','').strip() #removes newline simobls and strip " "

        digit = int(line.find(line.isdigit()))  #converts the number in digits
        sum_nums += digit

finally:
    exit(print(sum_nums))



