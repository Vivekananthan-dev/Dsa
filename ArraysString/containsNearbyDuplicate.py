def containDuplicate(nums,k):
    
    seen = {}

    for i,val in enumerate(nums):

        if val in seen and i-seen[val]<=k:
            return True
        seen[val] = i
        print(seen)
    
    return False

print(containDuplicate([1,4,3,1,2,3],2))
