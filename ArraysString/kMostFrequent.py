from collections import Counter

def top_k_frequent(nums, k):
    freq = Counter(nums)
    return [item for item, count in freq.most_common(k)]

print(top_k_frequent([1,1,1,2,2,3], 2))  
print(top_k_frequent([4,4,4,5,5,6,6,6,6], 2)) 
