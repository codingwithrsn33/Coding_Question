# Input: aaabbca
# Output: 3a2b1c1a

def run_encoding(s):
    if not s:
        return ""
        
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            result += str(count) + s[i-1]
            count = 1
    result += str(count) + s[-1]
    return result
print(run_encoding("aaabbccdd"))







# 📌 Run-Length Encoding (RLE) in Python

## 🔹 Problem Statement

Write a function that performs **Run-Length Encoding** on a given string.

Run-Length Encoding compresses a string by replacing consecutive repeated characters with:

```
count + character
```

---

## 🔹 Example

### Input:

```
aaabbccdd
```

### Output:

```
3a2b2c2d
```

---

# 🔹 Approach (Simple Logic)

1. If string is empty → return empty string.
2. Start counting from first character.
3. Loop through string from index 1.
4. Compare current character with previous character.
5. If same → increase count.
6. If different →

   * Add count + previous character to result
   * Reset count to 1
7. After loop ends →
   Add the last character group manually.

---

# 🔹 Why We Add Last Character Separately?

Inside loop, we only add characters when the character changes.

The last character group never gets added inside loop.

So we must add:

```python
result += str(count) + s[-1]
```

Without this line, last characters will be missing.

---

# 🔹 Code Implementation

```python
def run_encoding(s):
    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1

    # Add last character group
    result += str(count) + s[-1]

    return result


print(run_encoding("aaabbccdd"))
```

---

# 🔹 Dry Run (Step-by-Step)

Input:

```
aaabb
```

| Step        | Character | Count | Result |
| ----------- | --------- | ----- | ------ |
| a,a,a       | 3         |       |        |
| change to b |           |       | 3a     |
| b,b         | 2         |       | 3a     |
| End         |           |       | 3a2b   |

---

# 🔹 Time Complexity

```
O(n)
```

Because we traverse the string only once.

---

# 🔹 Space Complexity

```
O(n)
```

Because we create a new compressed string.

---

# 🔹 Edge Cases

1. Empty string → ""
2. Single character → "1a"
3. No repeating characters → "1a1b1c"

---

# 🔹 Interview Explanation (Short Version)

> I used a single loop to traverse the string.
> I counted consecutive repeating characters.
> When the character changed, I appended count and previous character to result.
> After loop completion, I added the last group manually.
> Time complexity is O(n).

---

