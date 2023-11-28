import heapq

def find_sets(intervals):

    heap = []

    intervals = sorted(intervals)
    # alternative to sorting
    # intervals.sort(key=lambda x: x[0])
    heap.append(intervals[0][1])
    heapq.heapify(heap)
    
    for i in range(1, len(intervals)):

        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)

        heapq.heappush(heap, intervals[i][1])
    
    return len(heap)


intervals = [[7,8],[1,2],[4,6],[3,4]]
find_sets(intervals)