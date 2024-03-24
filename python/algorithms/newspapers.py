def feasible(t, c, limit):
    print(t, c, limit)
    time = 0
    k = 0
    for r in t:
        if r + time > limit:
            time = 0
            k += 1
        time += r
    if time > 0:
        k += 1
    return k <= c


def newspapers_split(newspapers_read_times, num_coworkers):
    l, h = max(newspapers_read_times), sum(newspapers_read_times)
    print(l, h)
    ans = -1
    while l < h:
        m = (l + h) // 2
        if feasible(newspapers_read_times, num_coworkers, m):
            ans = m
            h = m - 1
        else:
            l = m + 1
    return ans


a = [1, 4, 4]

print(newspapers_split(a, 3))  # 4
