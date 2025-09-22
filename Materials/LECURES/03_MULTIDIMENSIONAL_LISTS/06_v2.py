#Find the position of a symbol 

n = int(input()) #dimestions of a matrix
symbol = input()  #speacial symobol

matrix = []
is_in = False

for  i in range(n):
    curr_row = list(input())
    if symbol in curr_row:
        position = curr_row.index(symbol) # returns the index of the posisiton of the value in the current col(col location)
        is_in = True
        print(f"({i},{position})") # prints the row,col cooordinates of the symbol in the matrix 

if not is_in:
    print(f'{symbol} does not occur in the matrix')

