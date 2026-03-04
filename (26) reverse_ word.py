def rev_word(n):
    reversed_char = ''
    for ch in n:
        reversed_char += ch
        result = reversed_char[::-1]
    return result
    
print(rev_word("suresh"))
         
    
         
