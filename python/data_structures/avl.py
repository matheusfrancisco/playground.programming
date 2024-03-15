import math


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return ""
        content = "\n"  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = " " * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0:
                break
            cur_row = " "
            next_row = ""
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:
                if n is None:
                    cur_row += "   " + sep
                    next_row += "   " + sep
                    next_nodes.extend([None, None])
                    continue

                if n.value is not None:
                    buf = " " * math.ceil(((5 - len(str(n.value))) / 2))
                    cur_row += "%s%s%s" % (buf, str(n.value), buf) + sep
                else:
                    cur_row += " " * 5 + sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += " /" + sep
                else:
                    next_row += "  " + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += "\ " + sep
                else:
                    next_row += "  " + sep
                    next_nodes.append(None)

            content += (
                cur_height * "   "
                + cur_row
                + "\n"
                + cur_height * "   "
                + next_row
                + "\n"
            )
            cur_nodes = next_nodes
            sep = " " * math.ceil(len(sep) / 2)  # cut separator size in half
        return content

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(f"value={cur_node.value}, h={str(cur_node.height)}")
            self._print_tree(cur_node.right)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left != None:
            return self._find(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._find(value, cur_node.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        ## ----- Protect against deleting a node not found in the tree

        if node is None or self.find(node.value) is None:
            print("Node to be deleted not found in the tree!")
            return None
        ## ----- returns the node with min value in tree rooted at input node

        def min_value_node(n):
            current = n
            while current.left != None:
                current = current.left
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left != None:
                num_children += 1
            if n.right != None:
                num_children += 1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to be deleted
        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:
            if node_parent != None:
                # remove reference to the node from the parent
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            # get the single child node
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node_parent != None:
                # replace the node to be deleted with its child
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right)
            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other nodes
            self.delete_node(successor)

            # exit function so we don't call the _inspect_deletion twice
            return

        if node_parent != None:
            # fix the height of the parent of current node
            node_parent.height = 1 + max(
                self.get_height(node_parent.left),
                self.get_height(node_parent.right),
            )
            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)
        return False

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent is None:
            return
        path = [cur_node] + path
        left_height = self.get_height(cur_node.parent.left)
        right_height = self.get_height(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return
        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    # for AVltree
    def _inspect_deletion(self, cur_node):
        if cur_node is None:
            return

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception("_rebalance_node: z,y,x node configuration not recognized!")

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.right)
        return cur_node.left if left >= right else cur_node.right


a = AVLTree()

for i in range(5):
    a.insert(i)
    print(a)
