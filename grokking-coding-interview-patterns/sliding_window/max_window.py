import collections



def find_max_sliding_window(arr, window_size):
    dq = collections.deque()

    out = []
    for i in range(len(arr)):
        dq.append(arr[i])
        if len(dq) >= window_size:
            m = max(dq)
            out.append(m)
            dq.popleft()

    return max(out)



assert(find_max_sliding_window([1, 2, 3, 4, 5, 6], 3) == 6)
