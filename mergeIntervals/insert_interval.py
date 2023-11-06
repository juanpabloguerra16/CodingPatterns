# Given a sorted list of nonoverlapping intervals and a new interval, 
# your task is to insert the new interval into the correct position 
# while ensuring that the resulting list of intervals remains sorted 
# and nonoverlapping. Each interval is a pair of nonnegative numbers, 
# the first being the start time and the second being the end time of the interval.

def insert_interval(existing_intervals, new_interval):

    i = 0
    n = len(existing_intervals)
    new_start, new_end = new_interval[0], new_interval[1]
    output = []

    while i < n and existing_intervals[i][0] < new_start:

        output.append(existing_intervals[i])
        i += 1

    if not output or output[-1][1] < new_start:
        output.append(new_interval)
    else:
        output[-1][1] = max(output[-1][1], new_end)

    while i < n:

        if output[-1][1] < existing_intervals[i][0]:
            output.append(existing_intervals[i])
        else:
            output[-1][1] = max(existing_intervals[i][1], output[-1][1])

        i += 1

    return output

print(insert_interval([[1,3],[4,5],[7,8],[9,12],[13,14]], [6,10]))




# def insert_interval(existing_intervals, new_interval):

#     if not existing_intervals or not new_interval:
#         return None
#     result = []
#     i = 0
#     new_start = new_interval[0]
#     new_end = new_interval[1]
    
#     while i < len(existing_intervals) and existing_intervals[i][0] < new_start:
#         result.append(existing_intervals[i])
#         i +=1

#     if not result or result[-1][1] < new_start:
#         result.append(new_interval)
#     else:
#         result[-1][1] = max(result[-1][1], new_end)

#     while i < len(existing_intervals):
        
#         if result[-1][1] < existing_intervals[i][0]:
#             result.append(existing_intervals[i])
#         else:
#             result[-1][1] = max(result[-1][1], existing_intervals[i][1])
#         i +=1
#     return result


# def insert_interval(intervals, new_interval):
#     merged_intervals = []
#     i = 0
#     n = len(intervals)
    
#     # Add intervals that come before the new interval
#     while i < n and intervals[i][1] < new_interval[0]:
#         merged_intervals.append(intervals[i])
#         i += 1
    
#     # Merge overlapping intervals with the new interval
#     while i < n and intervals[i][0] <= new_interval[1]:
#         new_interval[0] = min(new_interval[0], intervals[i][0])
#         new_interval[1] = max(new_interval[1], intervals[i][1])
#         i += 1
    
#     merged_intervals.append(new_interval)
    
#     # Add remaining intervals that come after the new interval
#     while i < n:
#         merged_intervals.append(intervals[i])
#         i += 1
    
#     return merged_intervals

# # Example usage:
# intervals = [[1, 3], [6, 9]]
# new_interval = [2, 5]
# result = insert_interval(intervals, new_interval)
# print(result)
