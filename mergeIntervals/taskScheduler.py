def least_time(tasks, n):
    
    frequencies = {}

    for t in tasks:
<<<<<<< HEAD
        frequencies[t] = frequencies.get(t, 0) + 1
    
    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    print(frequencies)
    max_freq = frequencies.popitem()[1]
    
    # max idle time = (max frequency - 1) x n = 6
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time = idle_time - min(max_freq -1, frequencies.popitem()[1])

    idle_time = max(idle_time, 0)

    return len(tasks) + idle_time

tasks = ['A', 'B', 'C', 'A', 'C']
n = 2

least_time(tasks, n)
=======
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

>>>>>>> 83178139e06c5a93beb923b8001150a143856e94
