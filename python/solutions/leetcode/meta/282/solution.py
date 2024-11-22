from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        # "1*2*3"

        def dfs(idx, cur_res, cur_sum, prev):
            if idx == len(num):
                if cur_sum == target:
                    res.append("".join(cur_res))
                    return
            else:
                for i in range(idx, len(num)):
                    cur_str = num[idx: i + 1]
                    cur_num = int(cur_str)
                    if not cur_res:
                        dfs(i + 1, [cur_str], cur_num, cur_num)
                    else:
                        dfs(i+1, cur_res + ["+"] + [cur_str], cur_sum + cur_num, cur_num)
                        dfs(i+1, cur_res + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)
                        dfs(i+1, cur_res + ["*"] + [cur_str], cur_sum - prev + cur_num * prev,
                            cur_num * prev)
                    if num[idx] == "0":
                        break
        dfs(0, "", 0, 0)
        return res
