#https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:  
    count=0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        val=None
        if root.left:
            val=self.kthSmallest(root.left,k)
        if val is not None:
            return val
        self.count+=1
        if self.count==k:
            return root.val
        if root.right:
            val=self.kthSmallest(root.right,k)
        return val
