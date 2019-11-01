#https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        q=[(root,0)]
        maxLen=0
        while len(q):
            maxLen=max(maxLen,q[-1][1]-q[0][1]+1)
            n=len(q)
            for i in range(n):
                node,idx=q.pop(0)
                if node.left:
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right,2*idx+1))
        return maxLen
