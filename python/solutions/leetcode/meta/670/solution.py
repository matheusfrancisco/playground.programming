import collections

class Solution1:
    def maximumSwap(self, num: int) -> int:
        # 2789 -> 9782
        # 9919 -> 9991
        # 10 --> 10
        # 101 -> 110
        # 198 -> 918 --> 981
        n = list(str(num))
        max_value = float("-inf")
        midx = -1
        swapi = -1
        swapj = -1
        #
        # 9973
        # 6415
        # max_value = 5
        # midx = 3
        # max_value = 5
        #
        for i in range(len(n) - 1, -1, -1):
            if max_value < int(n[i]):
                max_value = int(n[i])
                midx = i

            if int(n[i]) < m:
                swapi = i
                swapj = midx

        n[swapj], n[swapi] = n[swapi], n[swapj]

        return int("".join(n))

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num
        num_as_arr = collections.deque([])

        while num:
            num_as_arr.appendleft(num % 10)
            num //= 10
        max_seen = -1
        max_seen_at = len(num_as_arr)

        i = len(num_as_arr) - 1
        while i >= 0:
            cur_num = num_as_arr[i]
            # print(i,num_as_arr)
            num_as_arr[i] = (cur_num, max_seen, max_seen_at)
            # print(i,num_as_arr)
            if cur_num > max_seen:
                max_seen = cur_num
                max_seen_at = i
            i -= 1

        i = 0
        while i < len(num_as_arr):
            cur_num, max_to_right, max_seen_at = num_as_arr[i]
            if max_to_right > cur_num:
                num_as_arr[i], num_as_arr[max_seen_at] = num_as_arr[max_seen_at], num_as_arr[i]
                break
            i += 1

        num = 0
        for cur_num, _, _ in num_as_arr:
            num = num * 10 + cur_num
        return num
# O(N), n number of digits in number
# O(N), n number of digits
