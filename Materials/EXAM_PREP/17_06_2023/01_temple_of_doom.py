from collections import deque

tools  = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances:
    curr_tool = tools.popleft()
    curr_subst = substances.pop()

    mulitplier = curr_tool * curr_subst

    if mulitplier  in challenges:
        challenges.remove(mulitplier)
  
    else:
        curr_tool += 1
        tools.append(curr_tool)

        curr_subst -= 1
        if curr_subst > 0:
            substances.append(curr_subst)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him." )
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")

if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")