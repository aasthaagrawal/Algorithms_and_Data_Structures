#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
#Time Complexity: O(n)
#Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root, None, None)
        return self.res
        
    def traverse(self, node, par, gpar):
        if not node:
            return
        if gpar and gpar%2==0:
            self.res += node.val
        self.traverse(node.left, node.val, par)
        self.traverse(node.right, node.val, par)
