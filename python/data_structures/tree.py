
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self,value):
        def _insert(root,value):
            if value < root.value:
                if root.left is not None:
                    _insert(root.left, value)
                else:
                    root.left = Node(value)
            else:
                if root.right is not None:
                    _insert(root.right, value)
                else:
                    root.right = Node(value)

        if self.root is None:
            k = Node(value)
            self.root = k
        else:
            _insert(self.root, value)
        self.height += 1


    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.value)
                _inorder(root.right)
        if self.root:
            _inorder(self.root.left)
            print(self.root.value)
            _inorder(self.root.right)

def main():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    print(bst.inorder())

main()
# (out) 20
# (out) 30
# (out) 40
# (out) 50
# (out) 60
# (out) 70
# (out) 80
# (out) None
