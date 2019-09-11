#https://leetcode.com/problems/diameter-of-binary-tree/
#Complexity: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathLen(self,node):
        if not node:
            return 0
        left=self.pathLen(node.left)
        right=self.pathLen(node.right)
        self.maxSumInt=max(self.maxSumInt,left+right)
        return max(left,right)+1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxSumInt=0
        self.pathLen(root)
        return self.maxSumInt
