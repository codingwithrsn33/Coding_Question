# Input: "engineering"
# Output: e=3, i=2

def count_vowels(s):
    vowels="aeiouAEIOU"
    freq = {}
    for ch in s:
        if ch in vowels:
            freq[ch] = freq.get(ch,0) + 1
    return freq
        
print(count_vowels("engineering"))
        
