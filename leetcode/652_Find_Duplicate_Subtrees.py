#https://leetcode.com/problems/find-duplicate-subtrees/
#Time Complexity: O(n)
#Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.path_dict = defaultdict(int)
        self.res = []
        self.preorder(root)
        return self.res

    def preorder(self, node):
        if not node:
            return "#"
        path = str(node.val) + "," + self.preorder(node.left) + "," + self.preorder(node.right)
        self.path_dict[path] += 1
        if self.path_dict[path] == 2:
            self.res.append(node)
        return path
