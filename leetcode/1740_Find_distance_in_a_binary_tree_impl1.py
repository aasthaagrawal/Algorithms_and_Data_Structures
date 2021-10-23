#https://leetcode.com/problems/find-distance-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        self.result = None
        self.isResultSet = False
        self.traverseTree(root, p, q)
        return self.result

    def traverseTree(self, node, p, q):
        if not node:
            return False, 0
        mid = False
        if node.val == p or node.val == q:
            mid = True
        left, leftDist = self.traverseTree(node.left, p, q)
        if self.isResultSet: return True, 0
        right, rightDist = self.traverseTree(node.right, p, q)
        if self.isResultSet: return True, 0
        if left + right + mid >=2:
            self.result = leftDist + rightDist
            self.isResultSet = True
            return True, 0
        elif left + right + mid == 1:
            return True, leftDist + rightDist + 1
        return False, 0
