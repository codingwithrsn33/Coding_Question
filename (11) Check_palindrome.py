def check_palindrome(s):
    s = s.lower()   # case insensitive करण्यासाठी
    
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

print(check_palindrome("Madam"))
