def min_window(s, t):
    
    if t == "":
        return ""

    req_char = {}
    window = {}

    current, required = 0, len(t)

    for c in t:
        req_char[c] = 1 + req_char.get(c, 0)

    for c in t:
        window[c] = 0

    left = 0
    res, res_len = [-1, -1], float("infinity")
    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = 1 + window.get(c,0)

        if c in req_char and window[c] == req_char[c]:
            current += 1
        
        while current == required:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)
            
            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in req_char and window[s[left]] < req_char[s[left]]:
                current -= 1

            left +=1
    left, right = res
            
    return s[left:right+1] if res_len != float("infinity") else ""




# Given two strings, s and t, find the minimum window substring in s, which has the following properties:

# It is the shortest substring of s that includes all of the characters present in t.

# It must contain at least the same frequency of each character as in t.

# The order of the characters does not matter here.