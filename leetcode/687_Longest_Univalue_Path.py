#https://leetcode.com/problems/longest-univalue-path/
#Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        self.util(root)
        return self.result

    def util(self, node):
        if not node.left and not node.right:
            return 0
        larrow, rarrow = 0,0
        if node.left:
            llen = self.util(node.left)
            if node.left.val == node.val:
                larrow = llen + 1
        if node.right:
            rlen = self.util(node.right)
            if node.right.val == node.val:
                rarrow = rlen + 1
        self.result = max(self.result, larrow+rarrow)
        return max(larrow,rarrow)
