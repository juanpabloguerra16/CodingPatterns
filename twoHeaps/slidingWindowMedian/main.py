from heapq import *



def median_sliding_window(nums, k):
    

    min_heap = []
    max_heap = []
    medians = []

    for i in range(0,len(nums)):
        if len(nums) - i < k:
            break
        print(i+k-1) 
        for j in range(i, i+k):
            if not min_heap or -min_heap[0] > nums[j]:
                heappush(min_heap, -nums[j])
            elif not max_heap or max_heap[0] < nums[j]:
                heappush(max_heap, nums[j])
            if len(min_heap) > len(max_heap) + 1:
                heappush(max_heap, -heappop(min_heap))
            elif len(max_heap) + 1 > len(min_heap):
                heappush(min_heap, -heappop(max_heap))
        print(f"Min Heap: ${min_heap}")
        print(f"Max Heap: ${max_heap}")
        if k % 2 != 0:
            medians.append(-heappop(min_heap))
        else:
            m = -heappop(min_heap) / 2 + heappop(max_heap) / 2
            medians.append(m)
        
        min_heap.clear()
        max_heap.clear()

    return medians

def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    median = median_sliding_window(nums, k)
    print(f"${median}")


if __name__ == "__main__":
    main()