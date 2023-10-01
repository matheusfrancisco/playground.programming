from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root, out):
    if not root: 
        return
    out.append(root.val)
    preorder(root.left, out)
    preorder(root.right, out)

def make_tree_from_list(arr: list, i: int, n: int) -> TreeNode:
    root = None
    if i < n:
        val = arr[i]
        if val:
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
        preorder(tree, out)
        print(out)
    return 

main()
