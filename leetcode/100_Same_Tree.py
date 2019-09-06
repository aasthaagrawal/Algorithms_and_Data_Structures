#https://leetcode.com/problems/same-tree/
#Complexity=O(n) where n is min(number of nodes in p,number of nodes in q)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        elif not p and not q:
            return True
        return False
