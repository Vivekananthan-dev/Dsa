import math

def lcm_two(a, b):
    #Compute LCM of two numbers using GCD.
    return abs(a * b) // math.gcd(a, b)

def lcm_three(a, b, c):
    #Compute LCM of three numbers by reducing pairwise.
    return lcm_two(lcm_two(a, b), c)


n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

result = lcm_three(n1, n2, n3)
print("LCM of", n1, n2, n3, "is:", result)
