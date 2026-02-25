#  Input: "banana"
# Output: "ban"

def removing_dup(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
            
    return(result)
    
print(removing_dup("BANANA"))
