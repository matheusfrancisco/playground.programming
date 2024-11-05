

s = "lee(t(c)o)de)"


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0
        for c in s:
            if c == "(":
                res.append(c)
                cnt += 1
            elif c == ")":
                cnt -= 1
                if cnt >= 0:
                    res.append(c)
                else:
                    cnt = 0
            else:
                res.append(c)
        cnt = 0
        for i in range(len(res)-1, -1, -1):
            if res[i] == "(" and cnt <= 0:
                res.pop(i)
            elif res[i] == "(" and cnt > 0:
                cnt -= 1
            elif res[i] == ")":
                cnt += 1

        return "".join(res)


obj = Solution()
print(obj.minRemoveToMakeValid(s))
