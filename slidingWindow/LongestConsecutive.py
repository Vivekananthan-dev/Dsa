def longest_Consecutive(nums):
    n = set(nums)
    long = 0

    for num in n:

        if num-1 not in n:
            length =1
            while num + length in n:
                length +=1
            long = max(long,length)
    return long

val  = map(int,input("Enter a value: ").split())

print(longest_Consecutive(val))