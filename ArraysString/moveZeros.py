def moveZeroToEnd(arr):
    if len(arr)<2:
        return arr
    cur = 0
    for i in range(len(arr)):

        if arr[i]!=0:
            arr[i],arr[cur] = arr[cur],arr[i]
            cur+=1
    return arr

print(moveZeroToEnd([0,1,0,3,12]))
print(moveZeroToEnd([1,0,0,0,0]))
print(moveZeroToEnd([0,1]))
print(moveZeroToEnd([0]))