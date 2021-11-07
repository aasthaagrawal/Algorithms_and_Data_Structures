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
        closest = root.val
        while root:
            closest = min(root.val,closest,key = lambda x: abs(target-x))
            root = root.right if target>root.val else root.left
        return closest
