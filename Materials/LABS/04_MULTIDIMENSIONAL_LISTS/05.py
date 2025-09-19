rows,columns = map(int,input().split())

matrix = []

for i in range(rows):
    current_row = []
    for j in range(columns):
        # this one is complex we need 3 values per cell, 1st symbol is the the index of the row, the second - of the column, the third - of the row
        value = 97 + i #every  value is the ascii code the index converted into a characters as we need values from a,b..n
        print(f'{chr(value)}{chr(value + j)}{chr(value)}',end = ' ')
    print()
          