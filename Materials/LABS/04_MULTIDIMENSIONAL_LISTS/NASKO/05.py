r,c = [int(x) for x in input().split()]

start = ord('a')

for row in range(r):
    for col in range(c):
        print(f"{start + row}{start + col}{start + row}", end = '')
    print()