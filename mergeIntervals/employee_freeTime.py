import heapq
from interval import Interval

def employee_free_time(schedule):
    
    heap = []

    for i in range(len(schedule)):
        heap.append((schedule[i][0].start, i, 0))

    print(type(heap[0]))

    heapq.heapify(heap)

    result = []

    previous = schedule[heap[0][1]][heap[0][2]].start
    
    while heap:
        _, i, j = heapq.heappop(heap)
        selected_interval = schedule[i][j]
        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j+1].start,i,j+1))

        if selected_interval.start > previous:
            result.append(Interval(previous, selected_interval.startinterval))


        previous = max(previous, selected_interval.end)



    return result

def main():
    inputs = [
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
    ]
    i = 1
    for schedule in inputs:
        
        employee_free_time(schedule)


if __name__ == "__main__":
    main()


