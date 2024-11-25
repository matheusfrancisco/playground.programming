import collections
# O(3* N) -> O(N)
# O(N)
class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.defaultdict(int)
        max_freq = 0
        for char in s:
            count[char] += 1
            if max_freq < count[char]:
                max_freq = count[char]

        buckets = [[] for i in range(max_freq + 1)]
        for char, count in count.items():
            buckets[count].append(char)
        str_builder = []
        for i in range(max_freq, -1, -1):
            cur_bucket = buckets[i]
            if cur_bucket:
                for char in cur_bucket:
                    str_builder.append(char * i)

        return "".join(str_builder)
