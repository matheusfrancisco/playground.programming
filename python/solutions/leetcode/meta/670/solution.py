class Solution:
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
