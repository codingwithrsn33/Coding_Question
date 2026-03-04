# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

def count_word(words):
    # words = n.lower
      
    freq={}
    
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
            
    return freq
print(count_word(['apple', 'banana', 'apple', 'orange', 'banana']))
        
