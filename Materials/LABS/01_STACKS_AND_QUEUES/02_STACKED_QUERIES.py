from collections import deque 

number_queries = int(input())


stacky_chan = []


for curr_query in range(number_queries):

    query = input()

    if query.startswith('1'):
        _,number = query.split()
        number = int(number)
        stacky_chan.append(number)

    elif query.startswith('2') and stacky_chan:
        stacky_chan.pop()

    elif query.startswith('3'):
        print(max(stacky_chan))

    elif query.startswith('4'):
        print(min(stacky_chan))


while stacky_chan:
    if len(stacky_chan) == 1:
        print(stacky_chan.pop())
    else:
        print(stacky_chan.pop(),end = ', ')