from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.graph = {char: [] for word in words for char in word}

        for w1, w2 in zip(words, words[1:]):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    self.graph[w2[i]].append(w1[i])
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        white = set(self.graph.keys())
        black = set()
        grey = set()
        res = []
        while white:
            node = next(iter(white))
            if not self.dfs(white, black, grey, node, res):
                return ""
        return "".join(res)

    def dfs(self, white, black, grey, node, res):
        self.move_node(node, white, grey)
        for p in self.graph[node]:
            if p in black:
                continue
            if p in grey:
                return False
            if not self.dfs(white, black, grey, p, res):
                return False
        self.move_node(node, grey, black)
        res.append(node)
        return True

    def move_node(self, node, cur, target):
        cur.discard(node)
        target.add(node)
    # O(C) where C is the lenght of all strings in words added together
    # O(V+ E), where V is the number of vertexes and E is the number of edges
    # O(C + V + E)

    # Space
    # O(V + E)
