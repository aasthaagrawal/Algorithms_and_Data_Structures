#https://leetcode.com/problems/minimum-depth-of-binary-tree/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q=[]
        q.append(root)
        q.append("null")
        level=1
        while len(q):
            ele=q.pop(0)
            if ele=="null":
                level+=1
                if len(q) and not all(q)=="null":
                    q.append("null")
            else:
                if not ele.left and not ele.right:
                    break
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return level
