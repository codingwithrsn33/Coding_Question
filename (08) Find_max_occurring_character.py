# Input: "success"
# Output: s

def max_char(s):
    freq={}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
        
    max_char = None
    max_value = 0
    
    for ch in freq:
        if freq[ch] > max_value:
            max_value = freq[ch]
            max_char = ch
            
    return max_char 
    
print(max_char("success"))
    
        
