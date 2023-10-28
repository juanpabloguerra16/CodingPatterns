def find_longest_substring(input_str):
    if len(input_str) == 0:
        return 0

    longest_substring = 0

    window = {}
    left = 0
    window_length = 0

    for i in range(len(input_str)):
       
        if input_str[i] not in window:
            window[input_str[i]] = i
        else:
            if window[input_str[i]] >= left:
                window_length = i - left
                
                if window_length > longest_substring:
                    longest_substring = window_length

                left = window[input_str[i]] + 1
            window[input_str[i]] = i
        
        
    print(i)
    i += 1

    if longest_substring < i - left:
        longest_substring = i - left

    return longest_substring

print(find_longest_substring("conceptually"))


# Given a string, input_str, return the length of the longest substring without repeating characters.

