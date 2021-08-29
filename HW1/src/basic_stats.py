def avg(nums):
    return sum(nums) / len(nums)

def l_sqr(nums):
    return [num**2 for num in nums]

def var(nums):
    return sum([(x - avg(nums))**2 for x in nums]) / len(nums)
