from collections import deque

colous_string = deque(input().split())

main_colors = ["red","blue","yellow"]

secondary_colors = {
    'orange': ['ref','yellow'],
    'purple': ['ref','blue'],
    'green': ['yellow','blue'],
    }


collected_colors = []

while colous_string:
    first_str = colous_string.popleft()
    last_str = colous_string.pop() if colous_string else ""

    for color in  (first_str + last_str,last_str + first_str):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    
    else:
        first_sub = first_str[:-1] if first_str else ""
        last_sub = last_str[:-1] if last_str else ""

        middle = len(colous_string) //2
        

        if first_sub:
            colous_string.insert(middle,first_sub)
        
        if last_sub:
            colous_string.insert(middle,last_sub)

final_colors = []

for color in collected_colors:
    if color in secondary_colors:
        required = secondary_colors[color]
        if all(main in collected_colors for main in required):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)