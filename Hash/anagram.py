def anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    frq = {}
    for c in str1:
        frq[c] = frq.get(c,0)+1
    
    for c in str2:
        if c not in frq:
            return False
        frq[c] -=1
        if frq[c]<0:
            return False
    return True

print(anagram("listen","silent"))