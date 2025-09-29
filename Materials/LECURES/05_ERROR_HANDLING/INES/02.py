text = input()

try:
    times = int(input())
    print(text * times)
except:
    print('Variable times must be an integer')
