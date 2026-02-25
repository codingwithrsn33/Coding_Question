# Input: "silent", "listen"
# Output: True

def check_anagrams(s1, s2):
    if len(s1) != len(s2):
        print("ok")
        return False
    
    count = {}
    
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in s2:
        if ch in count:
            count[ch] -= 1
        else:
            return False
            
    for value in count.values():
        if value != 0:
            return False
         
    return True
            
print(check_anagrams("silent", "listen"))
            
    
