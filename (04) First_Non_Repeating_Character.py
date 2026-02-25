Input:  "aabbcddde"
Output: "c"

def character(s):
    for ch in s:
        if s.count(ch) == 1:
            return(ch)
            break
print(character("aabbcdde"))
