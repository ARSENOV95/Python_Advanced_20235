def multiply(*nums):
    result = 1
    for n in nums:
        result *= n
    
    return result

print(multiply(4, 5, 6, 1, 3))