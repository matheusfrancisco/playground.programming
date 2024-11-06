import heapq

def qsolution(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# print(qsolution([1, 2, 3, 5, 6], 2))


def countsort_kth(nums, k):
    max_num = max(nums)
    min_num = min(nums)
    count = [0] * (max_num - min_num + 1)

    for num in nums:
        count[num - min_num] += 1

    print(count)
    res = k
    for i in range(len(count)-1, -1, -1):
        res -= count[i]
        if res <= 0:
            return i + min_num
    return -1


print(countsort_kth([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4)
