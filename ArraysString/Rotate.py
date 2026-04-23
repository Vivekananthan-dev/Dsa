l = [1,2,3,4,5,6]
n =2
print("original values :",l)
for i in range(n):
    first = l[0]
    for j in range(len(l)-1):
        l[j]=l[j+1]
    l[len(l)-1]= first
print("first way: ", l)

#Another way
l = l[n:]+l[:n]
print("Second way: ", l)