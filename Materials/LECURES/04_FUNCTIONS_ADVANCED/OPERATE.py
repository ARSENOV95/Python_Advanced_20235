def operate (op :str,*args):
    for num in args:
        if not isinstance(num,int):
            return "Invalid integer"

    def addtion (nums):
        return sum(nums)
    
    def subtract(nums):
        diff = nums[0]
        for num in range(1,len(nums)):
            diff -= nums[num]
        return diff

    def multiplication(nums):
        product = 1
        for num in nums:
            product *= num
        return product

    def devision(nums):
        dev = nums[0]
        for num in range(1,len(nums)):
            dev /= nums[num]
        return dev

    if op == '+':
        return addtion(args)
    elif op == '-':
        return subtract(args)
    elif op == '*':
        return multiplication(args)
    elif op == '/':
        return devision(args)


print(operate("-", 2, 4, -2))