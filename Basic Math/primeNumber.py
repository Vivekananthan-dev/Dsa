def is_prime(num):

    prime = True
    
    if num <= 1:
        return "Not a prime"
    elif num == 2:
        return "Its prime"
    else:
        i = 2
        while i*i <= num:

            if num%i == 0:
                prime = False
                break
            i+=1
    if prime:
        return "Its prime"
    else:
        return "Not a prime"
    
val = int(input("Enter a number: "))

def primeNums(num):
    
    if num<2:
        return[]
    pr = [True]*(num+1)
    pr[0] = pr[1] = False
    i = 2
    while i*i <=num:
        if pr[i]:
            for j in range(i*i,num+1,i):
                pr[j] = False
        i +=1
    return [i for i in range(num+1) if pr[i]]

print(is_prime(val))
print(primeNums(47))
# Note: there is even more we can do by eliminating even numbers and also can even improve the code