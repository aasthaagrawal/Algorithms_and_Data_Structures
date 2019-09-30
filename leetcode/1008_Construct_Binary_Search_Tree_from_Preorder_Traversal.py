#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.index=0
        self.preorder=preorder
        low=min(preorder)
        high=max(preorder)
        return self.constructTree(low-1,high+1)
        
    def constructTree(self,low,high):
        if self.preorder[self.index]>low and self.preorder[self.index]<high:
            node=TreeNode(self.preorder[self.index])
            self.index+=1
            if self.index<len(self.preorder):
                node.left=self.constructTree(low,node.val)
            if self.index<len(self.preorder):
                node.right=self.constructTree(node.val,high)       
            return node
        return None
