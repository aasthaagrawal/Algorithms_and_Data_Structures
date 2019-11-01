#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validUtil(root,-float("inf"),float("inf"))
        
    def validUtil(self,node,llimit,rlimit):
        if not node:
            return True
        if llimit>=node.val or node.val>=rlimit:
            return False
        return self.validUtil(node.left,llimit,node.val) and self.validUtil(node.right,node.val,rlimit)
