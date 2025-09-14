expression = input()

stack = []

parenthesis = {"(":")",
               "{":"}",
               "[":"]"
}

for character in expression:
    if character in parenthesis.keys():
        stack.append(character)
    elif character in parenthesis.values():
        if not stack:
            print("NO")
            break
        
        last_opening_parenthesis = stack.pop()

        if parenthesis[last_opening_parenthesis] != character:
            print("NO")
            break
        
else:
    if stack:
        print("NO")
    else:
        print("YES")