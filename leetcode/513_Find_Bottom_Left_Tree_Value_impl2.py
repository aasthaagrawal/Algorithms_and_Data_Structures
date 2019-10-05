#https://leetcode.com/problems/find-bottom-left-tree-value/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        level=[root]
        result=None
        while level:
            nxtLevel=[]
            for node in level:
                if node.left:
                    nxtLevel.append(node.left)
                if node.right:
                    nxtLevel.append(node.right)
            if not nxtLevel:
                result=level[0].val
                break
            level=nxtLevel
        return result
