#https://leetcode.com/problems/find-distance-in-a-binary-tree/
#Complexity: O(V)

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
        count, dist = self.traverseTree(root, p, q)
        return dist

    def traverseTree(self, node, p, q):
        if not node:
            return 0, 0

        left_count, left_dist = self.traverseTree(node.left, p, q)
        right_count, right_dist = self.traverseTree(node.right, p, q)

        count = left_count + right_count + int(node.val in (p,q))
        dist = left_dist+right_dist
        if count==1:
            dist += 1
        return count, dist
