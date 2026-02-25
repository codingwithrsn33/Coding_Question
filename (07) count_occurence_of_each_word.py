# Input: "malayalam"
# Output: {'m':2,'a':4,'l':2,'y':1}

def count_word(s):
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0)+ 1
    return (freq)
    
print(count_word("malayalam"))



        
