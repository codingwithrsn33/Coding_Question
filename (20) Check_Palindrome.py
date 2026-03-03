# Input: [1,2,3,2,1] — Output: True

def check_palindrome(list1):
    reversed_list1 = (list1[::-1])
    
    if list1 == reversed_list1 :
        return True
    else :
        return False
        
print(check_palindrome([1,2,4,5,1,2,1]))
    
    
