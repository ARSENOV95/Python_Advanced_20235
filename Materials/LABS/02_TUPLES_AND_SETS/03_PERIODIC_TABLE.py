n = int(input())

elements = set()

for _ in range(n):
    element = input().split()
    if len(element) > 1:
        for el in element:
            elements.add(el)
    else:
        elements.add(element[0])

print(*elements, sep = '\n')