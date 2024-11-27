
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        l = 0
        n = 0
        while l < len(sentence):
            if sentence[l] == " ":

                if l + 1 > len(sentence) and n > 0:
                    return True
                else:
                    n += 1
                    end = sentence[l-1]
                    next_char = sentence[l+1]
                    if end != next_char:
                        return False
            l += 1
        if n == 0:
            if sentence[0] != sentence[len(sentence) - 1]:
                return False
        else:
            if sentence[0] != sentence[len(sentence) - 1]:
                return False
        return True

class Solution2:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[len(sentence) - 1]

class Solution3:
    def isCircularSentence(self, sentence: str) -> bool:
        
        l = 0
        while l < len(sentence):
            if sentence[l] == " " and sentence[l - 1] != sentence[l + 1]:
                return False
            l += 1
        return sentence[0] == sentence[len(sentence) - 1]
     
