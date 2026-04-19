# Return the first non repeating value
# Eg: "swiss" Traversal the entire string find the frequence 
# Output: "w" we can do traversal for frequency or use Counter in Collection

from collections import Counter

def firstNonRepeatchar(s):
    freq ={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1
    
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

print(firstNonRepeatchar("swiss"))

#Can add more constriant like this has case sensitive