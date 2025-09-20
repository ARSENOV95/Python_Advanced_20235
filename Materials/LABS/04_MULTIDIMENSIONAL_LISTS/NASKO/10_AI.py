# python
def spread_bunnies(mat, bunnies):
    rows, cols = len(mat), len(mat[0])
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in bunnies:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_bunnies.add((nr, nc))
    # mark new bunnies on the matrix and return updated set (old + new)
    for r, c in new_bunnies:
        mat[r][c] = "B"
    return mat, bunnies.union(new_bunnies)
 
 
rows, cols = [int(x) for x in input().split()]
matrix = []
p_row = p_col = None
bunnies = set()
 
for r in range(rows):
    row = list(input().strip())
    matrix.append(row)
    for c, ch in enumerate(row):
        if ch == "P":
            p_row, p_col = r, c
        elif ch == "B":
            bunnies.add((r, c))
 
commands = input().strip()
moves = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1),
}
 
has_won = False
is_dead = False
last_pos = (p_row, p_col)
 
for cmd in commands:
    nr, nc = moves[cmd](p_row, p_col)
    # remove player from current cell (he steps away or escapes)
    matrix[p_row][p_col] = "."
    # if move goes outside -> player escapes; keep last_pos as previous cell
    if not (0 <= nr < rows and 0 <= nc < cols):
        has_won = True
        last_pos = (p_row, p_col)
        # bunnies still spread this turn
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        break
 
    # move inside lair
    # if stepping into a bunny -> immediate death (but bunnies will still spread)
    if matrix[nr][nc] == "B":
        p_row, p_col = nr, nc
        is_dead = True
        # still spread bunnies after this turn
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        break
    else:
        # place player in new cell
        p_row, p_col = nr, nc
        matrix[p_row][p_col] = "P"
 
    # after the player's step, bunnies spread
    matrix, bunnies = spread_bunnies(matrix, bunnies)
 
    # if a bunny reached the player after spread -> dead
    if matrix[p_row][p_col] == "B":
        is_dead = True
        break
 
# print final lair
for row in matrix:
    print("".join(row))
 
if has_won:
    print(f"won: {last_pos[0]} {last_pos[1]}")
else:
    # if died while moving into a bunny, p_row/p_col is death cell
    print(f"dead: {p_row} {p_col}")