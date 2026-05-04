# Method 1 (Using Built in functionality - Slice)
def reverse_string(s):
    s=s.lower()
    result =""
    for ch in s:
         result += ch
         
    return result[::-1]
    
print (reverse_string("Suresh"))

# Method 2 (Without using built in functionality)

def reverse_string(s):
    s=list(s)
    
    left,right = 0 , len(s)-1
    
    while left < right:
        s[left] , s[right] = s[right] ,s[left]
        left = left + 1
        right = right -1
    
    return "".join(s)
    
print (reverse_string("Suresh"))
