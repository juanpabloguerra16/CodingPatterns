def min_window(str1, str2):
    size_str1, size_str2 = len(str1), len(str2)
    min_sub_len = float('inf')
    index_s1, index_s2 = 0, 0
    min_subsequence = ""
    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1
            if index_s2 == size_str2:
                start, end = index_s1, index_s1
                index_s2 -= 1
                while index_s2 >= 0:
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    start -= 1
                start += 1
                if end - start < min_sub_len:
                    min_sub_len = end - start
                    min_subsequence = str1[start:end+1]
                index_s1 = start
                index_s2 = 0
        index_s1 += 1
    return min_subsequence

# driver code
def main():
    str1 = ["abcdedeaqdweq", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["adeq", "kzed", "css", "la", "ab"]

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-"*100)

if __name__ == '__main__':
    main()



# Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.

# A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.

# Let’s say you have the following two strings:

# str1 = “abbcb”

# str2 = “ac”

# In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character b.