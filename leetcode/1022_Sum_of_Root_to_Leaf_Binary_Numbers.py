# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total=0
        if root:
            self.auxFunction(root,0)
        return self.total
        
    def auxFunction(self, root, sumTillNow):
        if not root.left and not root.right:
            self.total+=(2*sumTillNow)+root.val
            return
        
        sumTillNow=(2*sumTillNow)+root.val
        if root.left:
            self.auxFunction(root.left,sumTillNow)
        if root.right:
            self.auxFunction(root.right,sumTillNow)
