class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(tree: Node) -> Node:
    if tree is None:
        return None
    return Node(tree.val, invert_binary_tree(tree.right), invert_binary_tree(tree.left))
