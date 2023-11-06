def merge_intervals(intervals):
    if not intervals:
        return None
    result = []

    result.append([intervals[0][0],intervals[0][1]])
    
    for i in range(1, len(intervals)):

        last_added_interval = result[-1]
        prev_end = last_added_interval[1]

        if intervals[i][0] <= prev_end:
            result[-1][1] = max(intervals[i][1], prev_end)
        else:
            result.append([intervals[i][0], intervals[i][1]])
        
    return result


print(merge_intervals([ [2, 4], [3, 5], [4, 5], [6, 10], [12, 14] ]))