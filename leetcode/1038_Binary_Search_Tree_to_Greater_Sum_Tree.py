#https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.util(root,0)
        return root
    
    def util(self,root,sumtillnow):
        if root.right:
            sumtillnow=self.util(root.right,sumtillnow)
        sumtillnow+=root.val
        root.val=sumtillnow
        if root.left:
            sumtillnow=self.util(root.left,sumtillnow)
        return sumtillnow
