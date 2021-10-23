#https://leetcode.com/problems/invert-binary-tree/
#Time Complexity: O(V+E)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = [root]
        while q:
            node = q.pop(0)
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
