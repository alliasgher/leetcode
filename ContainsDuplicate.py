def hasDuplicate(nums: list[int]) -> bool:
    dict = {}

    for i in nums:
        if i in dict:
            return True
        dict[i] = 1
    
    return False
    
print(hasDuplicate([2,3,4,5]))