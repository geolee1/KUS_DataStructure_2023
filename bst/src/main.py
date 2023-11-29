# 자료구조개론 10주차 과제8
# BST 구현
#
# 미래모빌리티학과
# 2021271402 이지오


# import module
import sys      # for call main function
from typing import Any


# Binary Search Tree
class Node:
    def __init__(self, data:Any):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, root:int = None):
        self.root = None
        self.size = 0
        if root:
            self.insert(root)
            
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.size = 1
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                self.size += 1
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
                self.size += 1
            else:
                self._insert_recursive(node.right, data)
        else:
            raise ValueError(f"Duplicate value {data} found")

                    
    def inorder(self, node=None):
        if node is None:
            node = self.root
        result = ""
        if node:
            if node.left:
                result += self.inorder(node.left)
            if node.data:
                result += str(node.data) + " "
            if node.right:
                result += self.inorder(node.right)
        return result
    
    def preorder(self, node=None):
        if node is None:
            node = self.root
        result = ""
        if node:
            if node.data:
                result += str(node.data) + " "
            if node.left:
                result += self.preorder(node.left)
            if node.right:
                result += self.preorder(node.right)
        return result
    
    def postorder(self, node=None):
        if node is None:
            node = self.root
        result = ""
        if node:
            if node.left:
                result += self.postorder(node.left)
            if node.right:
                result += self.postorder(node.right)
            if node.data:
                result += str(node.data) + " "
        return result
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return self.generate_tree_string(self.root)
    
    def generate_tree_string(self, node:Node, depth_symbol:list = []):
        result = ""
        if node:
            result += str(node.data) + "\n"
            if node.right:
                if node.left:
                    result += "".join(depth_symbol) + "├r─"
                else:
                    result += "".join(depth_symbol) + "└r─"
                result += self.generate_tree_string(node.right, depth_symbol + ["│  "])
            if node.left:
                result += "".join(depth_symbol) + "└l─"
                result += self.generate_tree_string(node.left, depth_symbol + ["   "])
        return result
            
# define main function
def main(*args, **kwargs) -> int:    
    # [ 단계별 트리 구조 작성 ]
    # - (root = 33), 23, 15, 10, 9, 55, 87
    # root = 17은 수업에서 해서 33으로 변경하셨습니다.
    root = 33
    datas = [23, 15, 10, 9, 55, 87]
    print(f"(root = {root}), " + ", ".join([str(data) for data in datas]), end='\n\n')
    
    tree = BST(root)
    for data in datas:
        tree.insert(data)
        
    print(tree)
    
    # root = 5 일 경우는 과제에서 제외하셨습니다.
        
    # - Inorder traversal 결과는?
    inorder_result = tree.inorder()
    print(f"{inorder_result=}")
    
    # - Preorder traversal 결과는?
    preorder_result = tree.preorder()
    print(f"{preorder_result=}")
    
    # - Postorder traversal 결과는?
    postorder_result = tree.postorder()
    print(f"{postorder_result=}")
    
    print()
    
    return 0


# call main function
if __name__ == '__main__':
    sys.exit(main())ㅇ