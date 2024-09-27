class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca_on_bst(bst: Node, p: int, q: int) -> int:
    def dfs(root, path, i):
        if i.val == root.val:
            path.append(i)
            return path

        if i.val > root.val:
            pass

    return 0


bst = Node(
    8,
    Node(3, Node(1), Node(6, Node(4))),
    Node(
        10,
    ),
)

print(lca_on_bst(bst, 1, 6))
print(lca_on_bst(bst, 1, 6) == 3)
