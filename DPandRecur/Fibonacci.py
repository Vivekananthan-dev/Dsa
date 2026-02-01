class Recurssion:
    def findFib(self,n): # Time complexity :O(2^n) space complexity: O(n)
        if n ==1 or n==0:
            return n
        v=self.findFib(n-1)+self.findFib(n-2)
        return v


class Dp:
    def fib(self,n): # Time complexity :O(n) space complexity: O(n)(array+ recurrsion)
        dp = [-1]*(n+1)
        dp[0],dp[1]=0,1
        return self.compute(n,dp)
    def compute(self,n,dp): #top down approch 
        if dp[n] == -1:
            dp[n] = self.compute(n-1,dp) + self.compute(n-2,dp)
            return dp[n]
        return dp[n]
    def tabulationMethod(self,n): #Bottom up approch
        if n == 0 or n == 1: # Time complexity :O(n) space complexity: O(n)
            return n
        dp = [-1]*(n+1)
        dp[0],dp[1] =0,1
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n] 
        
# using regular method like curr,pre1,pre2 and adding both for current then swapping will makes O(1) space complexity with O(n) time  

s = Recurssion()
print(s.findFib(5-1))

v = Dp()
print(v.fib(6))
print(v.tabulationMethod(3))