# 10 Reverse a string using loop (interview favourite)
# suresh

def reversed_string(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
    return result[::-1]
            
print( reversed_string("suresh"))
