n = int(input())


intersection = []

for _ in range(n):
    ranges = input().split("-")

    r1 = set()
    r2 = set()

    for i in range(len(ranges)):
        start,end = list(map(int,ranges[i].split(",")))
        if i == 0:
            r1 = set(int(x) for x in range(start,end+1))
        else:
            r2 = set(int(x) for x in range(start,end+1))

        if len(r1 & r2) > len(intersection):
            intersection = list(r1 & r2)

print(f'Longest intersection is {intersection} with length {len(intersection)}')
