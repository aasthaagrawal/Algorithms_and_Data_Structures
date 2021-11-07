#https://leetcode.com/problems/closest-binary-search-tree-value/
#Time Complexity: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.pred = root.val
        self.succ = root.val
        self.target = target
        self.util(root)
        if abs(self.target-self.pred) < abs(self.succ-self.target):
            return self.pred
        else:
            return self.succ

    def util(self, node):
        if not node:
            return
        if self.target == node.val:
            self.pred = node.val
            self.succ = node.val
        elif self.target > node.val:
            self.pred = node.val
            self.util(node.right)
        else:
            self.succ = node.val
            self.util(node.left)
