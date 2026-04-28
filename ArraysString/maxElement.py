def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    if nums.count(candidate) > len(nums)//2:
        return candidate
    return None

print(majority_element([3,3,4,2,3,3,5])) 
print(majority_element([2,2,1,1,1,2,2])) 
