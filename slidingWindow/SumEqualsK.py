def SumEqualsK(arr,k):

    pre_sum = 0
    count = 0
    frq = {0:1}

    for i in arr:
        pre_sum +=i
        if (pre_sum-k) in frq:
            count +=frq[pre_sum-k]
        
        frq[pre_sum] = frq.get(pre_sum,0)+1
    return count

print(SumEqualsK([1, 1, 1], 2)) 