#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def auxInorder(self,node):
        if not node:
            return
        self.auxInorder(node.left)
        self.result.append(node.val)
        self.auxInorder(node.right)
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result=[]
        self.auxInorder(root)
        return self.result
