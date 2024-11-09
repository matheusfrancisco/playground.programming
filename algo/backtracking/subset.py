from typing import List

def subsets(nums: List[int]) -> List[List[int]]:

    n = len(nums)
    res = []

    def dfs(i, cur) -> None:
        if i == n:
            res.append(cur)
            return
        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)

    dfs(0, [])
    return res

def subsets2(nums: List[int]) -> List[List[int]]:

    res = []

    def dfs(i, path) -> None:
        res.append(path[:])
        for nidx in range(i, len(nums)):
            print(i)
            path.append(nums[nidx])
            print(path)
            dfs(nidx + 1, path)
            path.pop()

    dfs(0, [])
    return res


print(subsets2([1, 2, 3]))
