from collections import Counter

def findAnagrams(s,p):

    res = []

    p_count = Counter(p)
    windowCount = Counter()

    k = len(p)

    for i,ch in enumerate(s):

        windowCount[ch]+=1
        
        if i>=k:
            left = s[i-k]
            windowCount[left] -=1
            if windowCount[left] == 0:
                del windowCount[left]
            
        if windowCount == p_count:
            res.append(i-k+1)
    return res

print(findAnagrams("cbaebabacd", "abc"))
