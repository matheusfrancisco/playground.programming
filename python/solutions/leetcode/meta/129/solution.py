# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        def dfs(r, path):
            if r is None:
                return 0
            path = path * 10 + r.val
            if r.left is None and r.right is None:
                return path
            return dfs(r.left, path) + dfs(r.right, path)
        return dfs(root, 0)

    def sumNumbers1(self, root) -> int:
        paths = []

        def dfs(r, path):

            path.append(r.val)
            if r.left is None and r.right is None:
                n = 0
                for p in path:
                    n = n * 10 + p
                paths.append(n)
                return
            else:
                if r.left:
                    dfs(r.left, path)
                    path.pop()
                if r.right:
                    dfs(r.right, path)
                    path.pop()

            return
        dfs(root, [])
        return sum(paths)


t = TreeNode(1, TreeNode(2), TreeNode(3))
obj = Solution()
print(obj.sumNumbers(t))
