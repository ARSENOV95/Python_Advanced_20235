expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)

    if expression[i] == ')':
        start_index = stack.pop()
        end_idx = i + 1 # this is to avoid exclusivity
        print(expression[start_index:end_idx]) 


#what this does
#loops troug the string checking if thevalue on the given indx is  (
#if yes its tores it inot a stack, when a ) is encontered, then we remove the ( form the stacl and store it intp a variable, we add  1 to the idx of the )
#in the end we print  all thevalues from the string form the ( (new varaible) to ) inclusive
#we remvoed each opeing brackt, so if we have (()) the second ) will kon its opening pracket is the first (