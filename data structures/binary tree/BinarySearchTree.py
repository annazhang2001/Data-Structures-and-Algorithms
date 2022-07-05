class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



class BST(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def insert(self, new_val):
        self.insertHelper(self.root, new_val)

    def insertHelper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insertHelper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insertHelper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.searchHelper(self.root, find_val)

    def searchHelper(self, current, find_val):
        if current:
            if find_val == current.data:
                return True
            elif find_val > current.data:
                return self.searchHelper(current.right, find_val)
            elif find_val < current.data:
                return self.searchHelper(current.left, find_val)

        return False


bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))