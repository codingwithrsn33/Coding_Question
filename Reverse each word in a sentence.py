def reversed_words(s):
    words= s.split()
    reversed_words_ok=[]
    for word in words:
        reversed_words_ok.append(word[::-1])
    return " ".join(reversed_words_ok)

print (reversed_words("Hello World"))
