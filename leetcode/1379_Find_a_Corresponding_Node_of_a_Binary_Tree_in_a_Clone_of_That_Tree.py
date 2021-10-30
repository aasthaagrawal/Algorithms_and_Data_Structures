#https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
#Time complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None
        self.target = target
        self.util(original, cloned)
        return self.result

    def util(self, original, cloned):
        if not original:
            return
        if original == self.target:
            self.result = cloned
            return
        self.util(original.left, cloned.left)
        if not self.result:
            self.util(original.right, cloned.right)
