# find the highest multiple three multiple
# Sample 1 [1,2,3,4] -> 2*3*4 =24
# Sample 2 [-5,-2,-1,0,0,3,4,5] -> 3*4*5 = 60
# Sample 3 [-5,-2,-1,0,0,1,1,5] -> -5*-2*5 = 50
class Solution:
    # @param A: list of integers
    # return an integer 
    def findMax(self,l):
        l = sorted(l)
        if len(l)<3:
            return -1
        else:
            fi = l[-1]*l[-2]*l[-3]
            sec = l[0]*l[1]*l[-1]
            return max(fi,sec)

s=Solution()
inputval = list(map(int,input().split(",")))
print(s.findMax(inputval))