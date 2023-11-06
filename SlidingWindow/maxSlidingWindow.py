# Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) of size w.

# Game Plan:

# 1. Create a current_window varialble that holds the index of the nums list
# 2. Create an output variable that holder the max number of each window
# 3. Iterate through the nums list and compare inserted values with old values. Delete older if they are lower

def clean_up(x, current_window, nums):
    
    while current_window and nums[x] >= nums[current_window[-1]]:
        del current_window[-1]

def find_max_sliding_window(nums, w):
    
    output = []
    current_window = []
    if len(nums) == 0:
        return []

    if w > len(nums):
        w = len(nums)

    #iterate through the first window
    for x in range(w):

        clean_up(x, current_window, nums)
        current_window.append(x)
    
    output.append(current_window[0])

    #[1,5,4,5,23,523,2]
    # current window is 6
    # x = 8
    # w = 2
    # x-w = 6 drop current window 'del cw[0]'
    for x in range(w, len(nums)):
        clean_up(x, current_window, nums)
        current_window.append(x)
        if current_window and current_window[0] <= (x-w):
            del current_window[0]
        output.append(current_window[0])
    return output

# driver code
def main():
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput array:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

if __name__ == '__main__':
    main()
    
    

# [3,4,5,6]