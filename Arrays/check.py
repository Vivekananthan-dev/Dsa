l =[["v","s","h","vs"],["s","v"],["v","h","vs","hr","aa"]]
maxi = 0
c=0
for i in range(len(l)):
    maxi = max(maxi,len(l[i]))
    if maxi == len(l[i]):
        c = i
print(l[c])