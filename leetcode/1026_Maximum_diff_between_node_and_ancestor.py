#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
#Complexity: O(n)
#Space complexity = O(1) + recurssion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.util(root)[0]
    
    def util(self, node):
        if node.left==node.right==None:
            return [-1,node.val,node.val]
        result = [-1,node.val,node.val]
        if node.left:
            result = self.util(node.left)
            result[0]=max(result[0],abs(result[1]-node.val),abs(result[2]-node.val))
            if node.val<result[1]:
                result[1]=node.val
            if node.val>result[2]:
                result[2]=node.val
        if node.right:
            right_result = self.util(node.right)
            result[0]=max(result[0],right_result[0],abs(right_result[1]-node.val),abs(right_result[2]-node.val))
            if result[1]>right_result[1]:
                result[1]=right_result[1]
            if result[2]<right_result[2]:
                result[2]=right_result[2]
        return result
