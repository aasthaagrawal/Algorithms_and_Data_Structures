#https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.util(s,t,False)
        S
    def util(self,s,t,exact):
        if s==None and t==None:
            return True
        elif s==None or t==None:
            return False
        if exact:
            if s.val==t.val and self.util(s.left,t.left,exact) and self.util(s.right,t.right,exact):
                return True
            else:
                return False
        else:
            if s.val!=t.val:
                return self.util(s.left,t,exact) or self.util(s.right,t,exact)
            else:
                return (self.util(s,t,True)) or (self.util(s.left,t,exact) or self.util(s.right,t,exact)) 
