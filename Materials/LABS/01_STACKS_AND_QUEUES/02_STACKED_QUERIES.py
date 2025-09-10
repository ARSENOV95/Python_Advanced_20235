number_queries = int(input())


stacky_chan = []

for curr_query in range(number_queries):

    query = input()

    if query.startswith('1'):
        _,number = query.split()
        number = int(number)
        stacky_chan.append(number)

    elif query.startswith('2'):
        stacky_chan.pop()

    elif query.startswith('3'):
        print(max(stacky_chan))

    elif query.startswith('4'):
        print(min(stacky_chan))


print(stacky_chan)
