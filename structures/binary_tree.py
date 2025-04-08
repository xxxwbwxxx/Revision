class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, val)
    
    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if val == node.value:
                return True
            elif val < node.value:
                return _search(node.left, val)
            else:
                return _search(node.right, val)
        return _search(self.root, val)
    
    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)
        _inorder(self.root)
        return result
    

test = BinarySearchTree()   
test.insert(1)
test.insert(2)
test.insert(3)
test.insert(4)
print(test.search(1))
print(test.search(6))
print(test.inorder())