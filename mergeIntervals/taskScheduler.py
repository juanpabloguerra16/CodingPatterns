def least_time(tasks, n):
    
    frequencies = {}

    for t in tasks:
        if t in frequencies:
            frequencies[t] += 1
        else:
            frequencies[t] = 1

    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time -= min(max_freq-1, frequencies.popitem()[1])

    return len(tasks)+idle_time


Tasks = ['A', 'A', 'A', 'B', 'B', 'C', 'C']
n = 1

least_time(Tasks, n)







# Given the two input values, tasks and n, find the least number of units of time the CPU will take to perform the given tasks.

