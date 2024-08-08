from heapq import *
from min_heap import *
from max_heap import *

#naive approach:
# def maximum_capital(c, k, capitals, profits):

    #c is the capital 
    #k is how many iterations we can invest
    #capitals is the array of capitals required to generate profits

    #determine the max amount of profit that can be generated
#     projects = list(zip(capitals, profits))

#     current_capital = c
#     selected_projects = []

#     for i in range(k):
#         feasible_projects = [project for project in projects if project[0] <= current_capital]

#         if not feasible_projects:
#             break

#         selected_project = max(feasible_projects, key=lambda x: x[1])

#         selected_projects.append(selected_projects)
#         projects.remove(selected_project)
#         current_capital += selected_project[1]

    
#     return current_capital

# optimized solution using two heaps:

def maximum_capital(c, k, capitals, profits):
    
    current_capital = c
    capital_min_heap = []
    profit_min_heap = []

    for i in range(len(capitals)):
        heappush(capital_min_heap, (capitals[i], i))

    for _ in range(k):

        while capital_min_heap and (capital_min_heap[0][0] <= current_capital):
            c, i = heappop(capital_min_heap)
            heappush(profit_min_heap, -profits[i])

        if not profit_min_heap:
            break

        j = -heappop(profit_min_heap)
        current_capital += j

    return current_capital



def main():
    input = (
              (0, 1, [1, 1, 2], [1 ,2, 3]),
              (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
              (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
              (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
              (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
              (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()
          