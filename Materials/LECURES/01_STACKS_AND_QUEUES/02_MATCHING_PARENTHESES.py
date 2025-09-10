expression = input()

paranthesis = []

for i in range(len(expression)):
    if expression[i] == '(':
        paranthesis.append(i)
    elif  expression[i] == ')':
        open_bracket = paranthesis.pop()
        close_bracket = i + 1
        print(expression[open_bracket:close_bracket])

#What this does is whenever we find an opening bracket we store it in a list, using the stack principle, we append the opening brackets
#when we find the first closign bracket, it openign one will be the last index of an openign bracket in a list, we pop it ans store it
#we print the slice from the closing bracket to the stored opeing bracket,
#all this is done while looping trouigh the list and check checkin each value and storing the value's index