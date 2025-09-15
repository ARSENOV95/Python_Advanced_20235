elements = set()

for _ in range(int(input())):
    element = input().split()
    if len(input().split()) > 1:
        for el in element:
            elements.add(el)
    else:
        elements.add(element[0])

print(*elements, sep = '\n')