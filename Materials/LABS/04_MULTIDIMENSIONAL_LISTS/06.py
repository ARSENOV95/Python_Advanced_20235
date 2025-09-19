def val_points(p1 :int,p2:int,coor1 :list,coor2 :list)->bool:
    if coor1[0] < p1 and coor1[1] <  p2 and\
        coor2[0] < p1 and coor2[1] <  p2 and (coor1[0] > 0 and coor1[1] > 0 and coor2[0] and coor2[1]):

        return True

rows,cols = map(int,input().split())

matrix = [input().split() for _ in range(rows)]

while True:

    command_body = input().split()

    if command_body[0] == 'END':
        break
        
    c1 = [int(x) for x in command_body[1:3]]
    c2 = [int(x) for x in command_body[3:]]
    
    if not val_points(rows,cols,c1,c2) or command_body[0] != 'swap':
        print('Invalid input!')
        continue

    matrix[[c1[0]][c1[1]]]  =  matrix[[c2[0]][c2[1]]]

    print(matrix)

