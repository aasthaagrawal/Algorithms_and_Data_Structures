#https://leetcode.com/problems/symmetric-tree/
#Complexity: O(V+E)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        curr = [root]
        nextQ = []
        ls = []
        while len(curr) > 0:
            for node in curr:
                if node is not None:
                    ls.append(node.val)
                    if node.left:
                        nextQ.append(node.left)
                    else:
                        nextQ.append(None)
                    if node.right:
                        nextQ.append(node.right)
                    else:
                        nextQ.append(None)
                else:
                    ls.append(None)
            if ls != ls[::-1]:
                return False
            curr = nextQ
            nextQ=[]
            ls=[]
        return True
