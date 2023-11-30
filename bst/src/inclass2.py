class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
def inorderTraversal(root):
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right) if root else []

def preorderTraversal(root):
    return [root.data] + preorderTraversal(root.left) + preorderTraversal(root.right) if root else []

def postorderTraversal(root):
    return postorderTraversal(root.left) + postorderTraversal(root.right) + [root.data] if root else []

dataArray = [17, 23, 15, 10, 9, 55, 87]
root = Node(dataArray[0])

for data in dataArray[1:]:
    root.insert(data)

print("Inorder traversal result: ", inorderTraversal(root))
print("Preorder traversal result: ", preorderTraversal(root))
print("Postorder traversal result: ", postorderTraversal(root))