# Input: "hello hello world" — Output: {'hello':2,'world':1}

def count_word(n):
    freq={}
    words = n.split()
    
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            
    return freq
print(count_word("hello hello world"))
            
            
        
    
        
            
            
    
            
