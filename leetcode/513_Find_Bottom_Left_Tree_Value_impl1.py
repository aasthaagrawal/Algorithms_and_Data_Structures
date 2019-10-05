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
        q=[]
        q.append(root)
        q.append("null")
        result=None
        pick=True
        while len(q):
            ele=q.pop(0)
            if pick is True:
                result=ele.val
                pick=False
            if ele is "null":
                pick=True
                if len(q):
                    q.append("null")
            else:
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return result
