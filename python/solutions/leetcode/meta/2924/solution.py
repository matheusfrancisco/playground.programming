from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graphs = [0] * n

        for u, v in edges:
            graphs[v] += 1

        champ = -1
        champ_c = 0
        for i in range(n):
            if graphs[i] == 0:
                champ_c += 1
                champ = i

        if champ_c == 1:
            return champ

        return -1
