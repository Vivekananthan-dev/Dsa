#the algorithm is an greed + binary search

import bisect

def lengthOfSubsequence(nums):

    sub = []
    for num in nums:

        i = bisect.bisect_left(sub,num)
        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)

arr = list(map(int,input("Enter the value: ").split()))
print(lengthOfSubsequence(arr))