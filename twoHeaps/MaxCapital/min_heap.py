# Template for min_heap implementation

from heapq import *

class min_heap:
    def __init__(self):
        self.min_heap_list = []
        
    def insert(self, x):
        heappush(self.min_heap_list, x)

    def get_min(self):
        return self.min_heap_list[0]

    def __str__(self):
        out = "["
        for i in self.min_heap_list:
            out+=str(i) + ", "
        out = out[:-2] + "]"
        return out