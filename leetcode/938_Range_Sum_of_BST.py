#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root==None:
            return 0
        sum=0
        if L<=root.val<=R:
            sum+=root.val
        sum+=self.rangeSumBST(root.left,L,R) + self.rangeSumBST(root.right,L,R)
        return sum
