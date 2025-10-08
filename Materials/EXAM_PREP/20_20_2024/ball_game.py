from collections import deque as dq

GOAL =100


strength = list(map(int,input().split()))  #take last strghth LIFO
accuracy = dq(map(int,input().split())) #FIFO

scored_goals = 0


while strength and accuracy:
    sum_goal_acc = strength[-1]  + accuracy[0]

    if sum_goal_acc == GOAL:
        scored_goals += 1
        strength.pop()
        accuracy.popleft()
    
    elif sum_goal_acc < GOAL:
        if strength[-1] > accuracy[0]:
            accuracy.popleft()
            
        elif strength[-1] < accuracy[0]:
            strength.pop()

        elif strength[-1] == accuracy[0]: 
            strength[-1] += accuracy[0]
            accuracy.popleft()
        
    elif sum_goal_acc > GOAL:
        strength[-1] -= 10
        accuracy.rotate(-1)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif not scored_goals:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")
else:
    print("Goals scored: {total goals}")

if scored_goals:
    print(f'Goals scored: {scored_goals}')

if strength:
    print(f"Strength values left: {', '.join([str(x) for x in strength])}")

if accuracy:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracy])}")