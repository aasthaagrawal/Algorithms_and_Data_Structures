#https://leetcode.com/problems/insert-into-a-binary-search-tree/
#Time Complexity: O(h) where h is the depth of a bst which in worst case of a skewed tree might become equal to n
#Space Complexity: O(1) (recursive stack space not counted)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
        else:
            if val>root.val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)
        return root
