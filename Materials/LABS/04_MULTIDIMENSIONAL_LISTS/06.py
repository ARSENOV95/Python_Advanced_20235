def valid_range(r1 :int,c1 :int,r2 :int,c2 :int,mx):
    return 0<= r1 <= len(mx) and 0<= c1 <= len(mx[r1]) and 0<= r2 <= len(mx) and 0<= c2 <= len(mx[r2])
 
#used for the version with rows and columns , but waht if the meatrix has rows iwth different len of columns? It will work as it fits the max range
#def valid_range(r1 :int,c1 :int,r2 :int,c2 :int,r :int,c :int):
#return 0<= r1 <= r and 0<= c1 <= c and 0<= r2 <= r and 0<= c2 <= c)



rows,cols = map(int,input().split())

matrix = [input().split() for _ in range(rows)]

invalid = False

while True:

    command = input()

    if command.startswith('END'):
        break

    c_body = command.split()

    if  not (len(c_body) == 5 and c_body[0] == 'swap'):
        print('Invalid input!')
        continue

    row1,col1,row2,col2 = map(int,c_body[1:])

    #orignal
    if not (valid_range(row1,col1,row2,col2,matrix)):
        print('Invalid input!')
        continue

    #alterantive
    #use the number of rows and cols to check as they are the same as the values in the matrix 
    #    if not (valid_range(row1,col1,row2,rows,cols)):
    #    print('Invalid input!')
    #    continue

    matrix[row1][col1],matrix[row2][col2] = matrix[row2][col2],matrix[row1][col1]
    [print(*row) for row in matrix]
            




