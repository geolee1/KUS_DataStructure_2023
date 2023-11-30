class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recusive(self.root, data)
            
    def _insert_recusive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recusive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recusive(node.right, data)
        else:
            print("Data already exist")
            
    def inorderTraversal(self):
        def inorder(node):
            if node:
                return inorder(node.left) + [node.data] + inorder(node.right)
            return []
        return inorder(self.root)
    
    def preorderTraversal(self):
        def preorder(node):
            if node:
                return [node.data] + preorder(node.left) + preorder(node.right)
            return []
        return preorder(self.root)
    
    def postorderTraversal(self):
        def postorder(node):
            if node:
                return postorder(node.left) + postorder(node.right) + [node.data]
            return []
        return postorder(self.root)
    
dataArray = [17, 23, 15, 10, 9, 55, 87]
bst = BST()

for data in dataArray:
    bst.insert(data)
    
print("Inorder traversal result: ", bst.inorderTraversal())
print("Preorder traversal result: ", bst.preorderTraversal())
print("Postorder traversal result: ", bst.postorderTraversal())