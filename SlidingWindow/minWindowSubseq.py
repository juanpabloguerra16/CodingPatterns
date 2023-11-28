# Given two strings, str1 and str2, find the shortest substring in str1 such that 
# str2 is a subsequence of that substring.
# Let’s say you have the following two strings:

# str1 = “aabbcb”
# current_window 

# str2 = “ac”

# In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character b. 





def minWindowSub(string1: str, string2: str) -> str:
    "aababcd"
    "ac"
    i = 0
    subSeq = []

    for x in range(len(string1)):
        # print(f"str1[x]: {string1[x]} str2[0]: {string2[0]}")
        
        if i < len(string2):
            print(string2[0] == string1[x])
            if string1[x] == string2[i]:
                i += 1
                subSeq.append(string1[x])
            elif string2[0] == string1[x]:
                subSeq.clear()
                subSeq.append(string1[x])
                i = 1
            elif i > 0:
                subSeq.append(string1[x])
            
    if subSeq:
        return "".join(subSeq)
    else:
        return ""

result = minWindowSub("ababcd", "cd")
print(result)