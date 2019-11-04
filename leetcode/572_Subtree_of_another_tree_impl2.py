#https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t==None:
            return True
        if s==None:
            return False
        if s.val==t.val:
            result=self.areIdentical(s,t)
            if result:
                return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
    def areIdentical(self,s,t):
        if s==None and t==None:
            return True
        elif s==None or t==None:
            return False
        if s.val==t.val:
            return self.areIdentical(s.left,t.left) and self.areIdentical(s.right,t.right)
        else:
            return False
