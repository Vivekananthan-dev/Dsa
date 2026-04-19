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

print(is_prime(val))

# Note: there is even more we can do by eliminating even numbers and also can even improve the code