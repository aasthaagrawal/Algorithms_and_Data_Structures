#https://leetcode.com/problems/binary-tree-preorder-traversal/
#Time Complexity: O(n)
#Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            ele = stack.pop()
            res.append(ele.val)
            if ele.right:
                stack.append(ele.right)
            if ele.left:
                stack.append(ele.left)
        return res
