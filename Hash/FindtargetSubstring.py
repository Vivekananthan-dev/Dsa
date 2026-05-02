from collections import Counter

def find_Substring(s,t):
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    window_count = {}

    have,need = 0,len(t_count)
    res, res_len = [-1,-1],float("inf")
    left = 0
    
    for right, ch in enumerate(s):
        window_count[ch] = window_count.get(ch,0)+1

        if ch in t_count and window_count[ch] == t_count[ch]:
            have +=1
        
        while have == need:

            if (right-left+1)<res_len:
                res = [left,right]
                res_len = right - left +1
            
            window_count[s[left]] -=1
            if s[left] in t_count and window_count[s[left]] <t_count[s[left]]:
                have -=1
            left +=1
        
    l,r = res    
    return s[l:r+1] if res_len != float("inf") else " "

print(find_Substring("ADOBECODEBANC", "ABC"))
