import heapq

def k_Largest_value(num,k):

    high = []

    for n in num:
        heapq.heappush(high,n)

        if len(high) >k:
            heapq.heappop(high)
    return high[0]

nums = map(int,input("Enter the numbers: ").split())
k = int(input("Enter the Kth position: "))
print(k_Largest_value(nums,k))