class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Returns -1 if is not a balanced binary tree. The height if it is.
def tree_height(tree):
    if tree is None:
        return 0
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if left_height is -1 or right_height is -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height) + 1


def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1


def is_balanced2(tree: Node) -> bool:
    def dfs(n, balanced):
        if n is None:
            return 0, balanced

        left, bl = dfs(n.left, balanced)
        right, br = dfs(n.right, balanced)

        return max(left, right) + 1, abs(left - right) <= 1 and bl and br

    _, b = dfs(tree, True)

    return b


def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


tree = build_tree(iter("1 2 4 x x 5 x x 3 x 6 x x"), int)

if tree:
    print(is_balanced(tree))
    print(is_balanced2(tree))
