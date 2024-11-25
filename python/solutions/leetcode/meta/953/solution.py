from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.order = {letter: i for i, letter in enumerate(order)}

        for word1, word2 in zip(words, words[1:]):
            if not self.words_are_lexico(word1, word2):
                return False
        return True

    def words_are_lexico(self, word1, word2):
        for i in range(min(len(word1), len(word2))):
            if self.order[word1[i]] != self.order[word2[i]]:
                if self.order[word1[i]] < self.order[word2[i]]:
                    return True
                else:
                    return False
        return len(word1) <= len(word2)

# O(26) => O(1) + O(n) => O(M) where M is the length of the longest word
# O(1) , O(26)
