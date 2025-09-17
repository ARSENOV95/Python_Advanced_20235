from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

shakes = 0

while chocolates and cups_of_milk and shakes < 5: 
    #check 1 if both elements are <= 0 and continues, else checks separately which one is <0 and drops it, there is no noeed ofr elif
    # as after the first codntion which is True is executed it will contonei to the next itteration, we do not want to create a shake
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
       chocolates.pop()
       cups_of_milk.popleft()
       continue
    
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    ########if chocolates[-1] <= 0 or cups_of_milk[0] <= 0:  #will not work 1 if both are -5 it will only drop the first one and not the other one
    ########    if chocolates[-1] <= 0:
    ########        chocolates.pop()
    ########    elif cups_of_milk[0] <= 0:
    ########        cups_of_milk.popleft()
    
    #if both elements are equal the condition is satisfird and we have a shake
    if chocolates[-1] == cups_of_milk[0]:
        shakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    #else we rotate the first cup to the end and decrese the last chocolate by 5
    else:
        chocolates[-1] -= 5
        cups_of_milk.rotate(-1)
    
    

if shakes < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

#turns out while we cannot unpack in f string we cna peform a join as the result is string amnd not an itterable
# can use print within a print but its pointless if we print(', '.join(str(x) for x in chocolates) within the print we will have none, 
# the ayt its wirtten it passes the output of the if to the outer print
print(f"Chocolate: {', '.join(str(x) for x in chocolates) if chocolates else 'empty'}") 
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) if cups_of_milk else 'empty'}")
