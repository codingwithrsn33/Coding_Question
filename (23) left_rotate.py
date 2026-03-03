
def left_rotate(s,k):
    return s[k:] + s[ : k]
    
print(left_rotate("abcdef" , 2))

output =  cdefab
