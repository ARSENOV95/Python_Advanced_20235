string = list(input())

#while there are items in the list, pop every last one and print all of them o nthe same row
while string:
    print(string.pop(),end = '')


#notes:
#1.  list(string) != string.split()  there ios a diffrence, 
# if take a strign as an input for the list function, you will recieve a list with every char from the string
# string.split()  takes a string and splits it into a list with 1 or more characters by spaces
# 
# string = I Love Python
# list(string) = ['I', ' ', 'L', 'o', 'v', 'e', ' ', 'P', 'y', 't', 'h', 'o', 'n']
# 
# string.split() = ['I', 'Love', 'Python']
#