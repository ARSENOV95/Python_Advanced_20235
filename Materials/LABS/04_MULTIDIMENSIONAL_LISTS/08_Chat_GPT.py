import sys

def main():
    input = sys.stdin.readline

    line = input().strip()
    if not line:
        return
    try:
        n = int(line)
    except ValueError:
        return

    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        # Optionally ensure the row has length n; or you trust input
        matrix.append(row)

    # Read bomb coordinates
    coords_line = input().strip()
    bombs = []
    if coords_line:
        for pair in coords_line.split():
            x_str, y_str = pair.split(",")
            row = int(x_str)
            col = int(y_str)
            bombs.append((row, col))

    # Predefine neighbour offsets (including self if you want bomb to damage itself)
    neigh_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1), ( 0, 0), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    for row, col in bombs:
        # check within bounds (should be guaranteed), but also if bomb cell > 0
        if not (0 <= row < n and 0 <= col < n):
            continue
        if matrix[row][col] <= 0:
            # dead bombs can't explode
            continue

        val = matrix[row][col]

        # Affect neighbours
        for dr, dc in neigh_offsets:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] > 0:
                    matrix[nr][nc] -= val

        # After explosion, set bomb cell to zero
        matrix[row][col] = 0

    # After all bombs
    alive_count = 0
    alive_sum = 0
    for r in range(n):
        row_list = matrix[r]
        for v in row_list:
            if v > 0:
                alive_count += 1
                alive_sum += v

    print(f"Alive cells: {alive_count}")
    print(f"Sum: {alive_sum}")
    for r in range(n):
        print(*matrix[r])


if __name__ == "__main__":
    main()