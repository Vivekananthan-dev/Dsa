#Find the longest palindromic substring
class Solutions:
    def PalindromicSubstring(self,str):
        res = ""
        def expand(l,r):
            while l>=0 and r<len(str) and str[l]==str[r]:
                l -=1
                r +=1
            return str[l+1:r]
        for i in range(len(str)):
            even = expand(i,i+1)
            odd = expand(i,i)
            res = max(res,even,odd,key=len)
        return res

s = Solutions()
st = input()
print(s.PalindromicSubstring(st))
    