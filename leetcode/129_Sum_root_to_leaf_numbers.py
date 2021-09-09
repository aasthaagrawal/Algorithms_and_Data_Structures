#https://leetcode.com/problems/sum-root-to-leaf-numbers/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if root:
            self.util(0,root)
        return self.res
    
    def util(self,sum_till_parent,root):
        sum_till_parent = sum_till_parent*10 + root.val
        if not (root.left or root.right):
            self.res += sum_till_parent
            return
        if root.left:
            self.util(sum_till_parent,root.left)
        if root.right:
            self.util(sum_till_parent,root.right)
