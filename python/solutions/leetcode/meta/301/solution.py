from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()
        self.dfs(s, 0, [], 0, 0)
        return list(self.res)

    def dfs(self, string, cur_idx, cur_res, l_count, r_count):
        if cur_idx >= len(string):
            if l_count == r_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)
                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        else:
            cur_char = string[cur_idx]
            if cur_char == "(":
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count+1, r_count)
                cur_res.pop()

                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
            elif cur_char == ")":
                self.dfs(string, cur_idx+1, cur_res, l_count, r_count)
                if l_count > r_count:
                    cur_res.append(cur_char)
                    self.dfs(string, cur_idx + 1, cur_res, l_count, r_count + 1)
                    cur_res.pop()
            else:
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, l_count, r_count)
                cur_res.pop()
