def min_sub_array_len(target, nums):

    if len(nums) == 0:
        print("here")
        return 0

    min_sub_array = []
    min_len = float('inf')
    for n in nums:
        min_sub_array.append(n)
        while sum(min_sub_array) >= target:
            print(min_sub_array)
            min_len = min(min_len, len(min_sub_array))
            min_sub_array.pop(0)

    
    if min_len != float('inf'):
        return min_len
    
    return 0

    # Replace this placeholder return statement with your code
    
print(min_sub_array_len(7 , [2, 3, 1, 2, 4, 3]))