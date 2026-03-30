def unique(s):
    left = 0
    ans =""
    bag = set()
    
    for right in range(len(s)):
        while s[right] in bag:
            bag.remove(s[left])
            
            left +=1
        bag.add(s[right])
        
        if len(s[left:right+1]) > len(ans):
            ans =(s[left:right +1])
    
    return ans
    
print(unique("abcdeab"))
        
