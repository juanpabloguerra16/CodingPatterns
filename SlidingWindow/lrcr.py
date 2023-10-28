# Longest Repeating Character Replacement

# Given a string, s, of lowercase English characters and an integer, k, 
# return the length of the longest substring after replacing at most k 
# characters with any other lowercase English character so that all the 
# characters in the substring are the same.

def longest_repeating_character_replacement(s, k):
    string_length = len(s)
    length_of_max_substring = 0
    start = 0
    char_freq = {}
    most_freq_char = 0

    for end in range(string_length):
        if s[end] not in char_freq:
            char_freq[s[end]] = 1
        else:
            char_freq[s[end]] += 1

        most_freq_char = max(most_freq_char, char_freq[s[end]])

        if end - start + 1 - most_freq_char > k:
            char_freq[s[start]] -= 1
            start += 1
        
        length_of_max_substring = max(end - start + 1, length_of_max_substring)
        
    return length_of_max_substring

# Driver code
def main():
    input_strings = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    values_of_k = [2, 1, 1, 2, 4]

    for i in range(len(input_strings)):
        print(i+1, ".\tInput String: ", input_strings[i], sep="")
        print("\tk: ", values_of_k[i], sep="")
        print("\tLength of longest substring with repeating characters: ", longest_repeating_character_replacement(input_strings[i], values_of_k[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()

    