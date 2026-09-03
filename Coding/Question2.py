'''
Coding Q2 - Longest Substring Without Repeating Characters
'''

def len_longest_substring(s):
    last ={}
    left=0
    best =0

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left= last[ch]+1
        
        last[ch] = right
        best =max(best, right-left+1)
    
    return best
    
s=input()
print(len_longest_substring(s))
