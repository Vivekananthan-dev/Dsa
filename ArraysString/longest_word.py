def longest_word(s):
    word = s.split()
    return max(word,key=len)

s = input()
print(longest_word(s))