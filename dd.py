
# check the given number is palindrome or not
class Solutions:
    def palindrome(self,num):
        temp = num
        rev =0
        while temp>0:
            rem = temp%10
            rev = rev*10+rem
            temp = temp // 10
        if num == rev:
            return "Palindrome"
        else:
            return "Not a palindrome"

s = Solutions()
n = int(input())
print(s.palindrome(n))