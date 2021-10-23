#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
#Time Complexity: O(V)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        self.traverseTree(root, p, q)
        return self.lca

    def traverseTree(self, root, p, q):
        if not root:
            return False
        mid = False
        if root == p or root == q:
            mid = True
        left = self.traverseTree(root.left, p, q)
        right = self.traverseTree(root.right, p, q)
        if left + right + mid >= 2:
            self.lca = root
        return mid or left or right
