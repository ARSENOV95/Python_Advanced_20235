class ValueCannotBeNegative(Exception):
        pass
        """Raise when value is negative"""
        

numbers = 5

for num in range(numbers):
    curr_num = int(input())
    if curr_num >= 0:
         print(curr_num)
    else:
         raise ValueCannotBeNegative






