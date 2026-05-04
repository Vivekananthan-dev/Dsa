# These sorting method use three pointers low,mid,high also use three variable eg:0,1,2

def sort_d(nums):
    low,mid,high = 0,0,len(nums)-1

    while mid<= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low +=1
            mid +=1
        
        elif nums[mid] == 1:
            mid +=1
        
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -=1

arr = list(map(int,input("Enter the value: ").split()))

sort_d(arr)
print(arr)

