import heapq
import collections

class Solution:
    # T: O(nlogn)
    # S: O(N)
    def reorganizeString(self, s: str) -> str:
        s_counts = collections.Counter(s)
        heap = [(-count, char) for char, count in s_counts.items()]
        heapq.heapify(heap)

        res = []

        while len(heap) >= 2:
            top_count, top_char = heapq.heappop(heap)
            next_count, next_char = heapq.heappop(heap)
            res.append(top_char)
            res.append(next_char)

            if top_count + 1:
                heapq.heappush(heap, (top_count + 1, top_char))
            if next_count + 1:
                heapq.heappush(heap, (next_count + 1, next_char))
        if heap:
            top_count, top_char = heapq.heappop(heap)

            if res and top_count == -1 and not top_char == res[-1]:
                res.append(top_char)
            elif not res and top_count == -1:
                res.append(top_char)
                return "".join(res)
            else:
                return ""
            return "".join(res)
        return "".join(res)
