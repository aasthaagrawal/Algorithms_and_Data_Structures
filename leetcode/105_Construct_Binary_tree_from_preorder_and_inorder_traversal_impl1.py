#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
#Time complexity = O(n) where n is the number of nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        self.preorder = preorder
        self.inorder = inorder
        return self.util(0,len(self.inorder)-1)

    def util(self, start_i, end_i):
        if start_i > end_i:
            return None
        node = TreeNode(self.preorder[self.preorder_index], None, None)
        i = start_i
        while i<=end_i:
            if self.inorder[i] == self.preorder[self.preorder_index]:
                break
            i += 1
        self.preorder_index += 1
        node.left = self.util(start_i, i-1)
        node.right = self.util(i+1, end_i)
        return node
