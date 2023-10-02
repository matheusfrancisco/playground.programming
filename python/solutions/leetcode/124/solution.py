from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_from_list(arr: list, i: int, n: int) -> TreeNode:
    root = None
    if i < n:
        val = arr[i]
        if val:
            root = TreeNode(val)
            root.left =  make_tree_from_list(arr, (2*i)+1, n)
            root.right = make_tree_from_list(arr, (2*i)+2, n)
    return root


def path_sum(tree):
    out = [tree.val]
    def dfs(root):
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        left = max(left, 0)
        right = max(right, 0)
        out[0] = max(out[0], left+right+root.val)

        return max(left, right) + root.val
    dfs(tree)
    return out[0]

def main():
    n = int(input())
    for i in range(n):
        l = []
        inp = input().split(" ")
        for i in inp:
            if i == 'None':
                l.append(None)
            else:
                l.append(int(i))
        tree = make_tree_from_list(l, 0, len(l))
        s = path_sum(tree)
        print(s)
    return 

main()
