from typing import List
import collections

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        q = collections.deque([s])
        visited = set()

        while q:
            word = q.popleft()
            if word in visited:
                continue
            else:
                if not word:
                    return True
                visited.add(word)
                for start_word in wordDict:
                    if word.startswith(start_word):
                        q.append(word[len(start_word):])
        return False

# T: O(N) * O(N)* O(N) -> O(N^3)
# S: O(N)
