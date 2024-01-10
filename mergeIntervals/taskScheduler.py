def least_time(tasks, n):
    
    frequencies = {}

    for t in tasks:
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