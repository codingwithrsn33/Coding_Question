def is_balanced(n):
    stack = []
    pairs = { ')' : '(', ']' : '[', '}': '{'}
    
    for ch in n:
        if ch in ("([{"):
            stack.append(ch)
        elif ch in (")]}"):
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0
                
print(is_balanced("[()]"))
                
                
            
