from collections import deque as dq

money = [int(x) for x in input().split()]
prices = dq(int(x) for x in input().split())

total_food = len(prices)
food_count = 0

while money and prices:
    curr_money = money[-1]
    curr_price = prices[0]

    if curr_money == curr_price:
        money.pop()
        prices.popleft()

    elif curr_money > curr_price:
        if len(money) > 1:
            difference = money.pop() - prices.popleft()
            money[-1] += difference
        else:
            money[-1] -= prices.popleft()

    elif curr_money < curr_price:
        money.pop()
        prices.popleft()   
        continue   

    food_count += 1


if  food_count == total_food:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")

elif food_count < total_food and food_count != 0:
    if food_count > 1:
        print(f"Henry ate: {food_count} foods.")
    else:
        print(f"Henry ate: {food_count} food.")

elif not food_count:
    print("Henry remained hungry. He will try next weekend again.")

