# Given a array of integer with an target integer value find the subarray
class Solution:
    def Subarray(self,arr,n):
        l,r=0,1
        sum = arr[l]+arr[r]
        size = r-l
        if arr[l] == n or arr[r] == n:
            return [l,size] if arr[l] == n else [r,size] 
        while r<len(arr):
            size = r-l
            if sum == n:
                return[l,r,size+1]
            elif sum<n:
                r+=1
                sum +=arr[r]
            elif sum>n:
                sum -=arr[l]
                l+=1
        return [-1,-1,-1]

s = Solution()
arr = list(map(int,input().split()))
n = int(input())
print(s.Subarray(arr,n))

