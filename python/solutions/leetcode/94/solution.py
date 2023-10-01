from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: Optional[TreeNode], out) -> list:
    if root is None: 
        return
    inorder(root.left, out)
    if root.val:
        out.append(root.val)
    inorder(root.right, out)


def make_tree_from_list(arr: list, i: int, n: int) -> TreeNode:
    root = None
    if i < n:
        val = arr[i]
        root = TreeNode(val)
        root.left =  make_tree_from_list(arr, (2*i)+1, n)
        root.right = make_tree_from_list(arr, (2*i)+2, n)
    return root



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
        out = []
        inorder(tree, out)
        print(out)
    return 

main()
