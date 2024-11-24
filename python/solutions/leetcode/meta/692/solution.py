from typing import List
import collections
import heapq

# O(N + N) = O(N)
# O(N + N) = O(N)

class HeapItem:
    def __init__(self, word: str, count: int) -> None:
        self.word = word
        self.count = count

    def __lt__(self, to_compare) -> bool:
        if self.count == to_compare.count:
            return self.word > to_compare.word
        return self.count < to_compare.count

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        heap = []
        res = []
        for word, count in freq.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)
        while k:
            cur = heapq.heappop(heap)
            res.append(cur.word)
            k -= 1
        res = list(reversed(res))
        return res
