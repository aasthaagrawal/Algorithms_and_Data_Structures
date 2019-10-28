#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        q=[]
        q.append(root)
        q.append("null")
        level=1
        maxSum=-float("inf")
        maxLevel=1
        curSum=0
        while len(q):
            ele=q.pop(0)
            if ele=="null":
                if maxSum<curSum:
                    maxSum=curSum
                    maxLevel=level
                level+=1
                curSum=0
                if len(q) and not all(q)=="null":
                    q.append("null")
            else:
                curSum+=ele.val
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return maxLevel
        
