matrix = [list(input()) for _ in range(int(input()))] 

search_symbol = input()

is_located = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if search_symbol == matrix[i][j]:
            is_located = True
            print(f'({i}, {j})')
            break
    if is_located:
        break

if not is_located:
    print(f'{search_symbol} does not occur in the matrix')