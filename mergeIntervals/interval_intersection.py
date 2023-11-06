# For two lists of closed intervals given as input, interval_list_a and interval_list_b, 
# where each interval has its own start and end time, write a function that returns the 
# intersection of the two interval lists.




def intervals_intersection(interval_list_a, interval_list_b):
    
    output = []
    a, b = 0, 0

    while a < len(interval_list_a) and b < len(interval_list_b):
        start_a, end_a = interval_list_a[a][0], interval_list_a[a][1]
        start_b, end_b = interval_list_b[b][0], interval_list_b[b][1]
        start_max = max(start_a, start_b)
        end_min = min(end_a, end_b)
        
        if start_max <= end_min: 
            output.append([start_max, end_min])

        if end_a < end_b:
            a += 1
        else:
            b +=1

    return output