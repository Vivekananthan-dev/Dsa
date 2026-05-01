from collections import defaultdict

def group_Shifted(s):

    group = defaultdict(list)
    for i in s:
        sig = []
        for j in range(1,len(i)):
            diff = (ord(i[j])-ord(i[j-1]))
            sig.append(diff)
        group[tuple(sig)].append(i)

    return list(group.values())

s = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(group_Shifted(s))