def is_prime(num):
    if num<=1:
        return False
    if num == 2 or num == 3:
        return True
    
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def primeFactors(num):

    if num <2:
        return []
    i =2
    ls = []
    while i*i<=num:
        if num%i ==0:
            if is_prime(i):
                ls.append(i)
            if num//i != i:
                if is_prime((num//i)):
                    ls.append(int(num//i))
        i+=1
    return sorted(ls)

print(primeFactors(60))
            