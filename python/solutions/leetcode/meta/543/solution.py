

def diameterOfBinaryTree(root):
    res = [0]

    def dfs(node):
        if not node:
            return -1

        left = dfs(node.left)
        right = dfs(node.right)
        res[0] = max(res[0], left + right + 2)
        return 1 + max(left, right)

    dfs(root)
    return res[0]


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)
# O(N)
