#https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        return self.equalToDescendantsUtil(root)[0]

    def equalToDescendantsUtil(self, node):
        if not node:
            return 0,0 #numNode,sum
        leftNum, leftSum = self.equalToDescendantsUtil(node.left)
        rightNum, rightSum = self.equalToDescendantsUtil(node.right)
        totalNum, totalSum = leftNum + rightNum, leftSum + rightSum
        if node.val == totalSum:
            totalNum += 1
        return totalNum, totalSum + node.val
