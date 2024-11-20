import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord or not wordList or endWord not in wordList:
            return 0
        graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                transform = word[:i] + "*" + word[i+1:]
                graph[transform].append(word)

        queue = collections.deque([(beginWord, 1)])
        seen = set()

        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            seen.add(word)
            for i in range(len(word)):
                transformed = word[:i] + "*" + word[i+1:]
                future_words = graph.get(transformed, None)
                if future_words:
                    for future_word in future_words:
                        if future_word not in seen:
                            queue.append((future_word, distance + 1))

        return 0
