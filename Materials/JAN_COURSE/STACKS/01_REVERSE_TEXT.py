string = list(input()) #you can directly input a list

#while the list len is > 0 pop out the last item, display aevery input on the same line 
while string:
    print(string.pop(),end='')