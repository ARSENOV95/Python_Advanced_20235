file modes 

r - read - opens a file for rading 

w - write opne the file for wirting

file.write('text') - if a file exeists its truncates it and appends 'text' into the file
==============================

a - append - adds text to the end of the line or on a new line if \n is added

example.txt:
text

open('example.txt,'a') as file
file.write('text1')

=
texttext1

file.write('\ntext1')

=
text
text1

w+,r+,a+ - opens the file in read-write

#only for rrad the file needs to exist in order to not havre a FileNotFound Error
#if not exesitend if opended in W mode it will create the file