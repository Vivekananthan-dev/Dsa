#Median of Two Sorted Arrays 

def findMedian(num1,num2):

    a,b = num1,num2

    if len(a)>len(b):
        a,b = b,a
    
    total = len(a)+len(b)
    half = total // 2
    l,r = 0,len(a)-1

    while True:
        i = (l+r)//2
        j = half-i-2

        al = a[i] if i>=0 else float("-inf")
        ar = a[i+1] if (i+1)<len(a) else float("inf")
        bl = b[j] if j>=0 else float("-inf")
        br = b[j+1] if (j+1)<len(b) else float("inf")

        if al <=br and bl<=ar:

            if total%2:
                return min(ar,br)
            return (max(al,bl)+min(ar,br)) / 2
        elif al>br:
            r = i-1
        else:
            l = i +1

n1 = list(map(int,input("Enter the values in n1: ").split()))
n2 = list(map(int,input("Enter the values in n2: ").split()))

print(findMedian(n1,n2))

        