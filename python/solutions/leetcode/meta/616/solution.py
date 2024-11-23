from typing import List

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        bold_status = [False] * len(s)
        # "abcxyz123"
        # ["abc","123"], 0, 3, 0 + 3= 3
        for word in words:
            start = s.find(word)
            length = len(word)
            while start != -1:
                for i in range(start, start + length):
                    bold_status[i] = True
                start = s.find(word, start + 1)
        i = 0
        string_builder = []
        while i < len(s):
            if bold_status[i]:
                string_builder.append("<b>")
                while i < len(s) and bold_status[i]:
                    string_builder.append(s[i])
                    i += 1
                string_builder.append("</b>")
            else:
                string_builder.append(s[i])
                i += 1
        return "".join(string_builder)
