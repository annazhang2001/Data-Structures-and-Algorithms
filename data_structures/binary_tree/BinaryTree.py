class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        else:
            print("Invalid type")

    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal


tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)

tree.root.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.left.left = Node(7)

print(tree.print_tree("postorder"))