#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
#Complexity: O(numOfNodes)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        maxSum=-float("inf")
        maxLevel=0
        level=1
        curLevelq=[root]
        nextLevelq=[]
        while len(curLevelq):
            curSum=0
            for node in curLevelq:
                curSum+=node.val
                if node.left:
                    nextLevelq.append(node.left)
                if node.right:
                    nextLevelq.append(node.right)
            if curSum>maxSum:
                maxSum=curSum
                maxLevel=level
            level+=1
            curLevelq=nextLevelq[:]
            nextLevelq=[]
        return maxLevel
