
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t = TreeNode(1,
             TreeNode(2, None, TreeNode(5)),
             TreeNode(3, None, TreeNode(4)))


def rightSideView(root):
    if root is None:
        return []

    r = []

    def helper(node, level):
        if level == len(r):
            r.append(node.val)
        for c in [node.right, node.left]:
            if c:
                helper(c, level + 1)
    helper(root, 0)
    return r


print(rightSideView(t) == [1, 3, 4])
