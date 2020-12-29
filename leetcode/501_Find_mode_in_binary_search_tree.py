#https://leetcode.com/problems/find-mode-in-binary-search-tree/
#Time complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.curNum = None
        self.curNumCount = -float("inf")
        self.modeVal = -float("inf")
        self.modeArr = set()
        self.inorder(root)
            
        return list(self.modeArr)
    
    def inorder(self, node):
        if node.left:
            self.inorder(node.left)
        
        if self.curNum!=node.val:
            if self.curNumCount > self.modeVal:
                self.modeVal = self.curNumCount
                self.modeArr = {self.curNum}
            elif self.curNumCount == self.modeVal:
                self.modeArr.add(self.curNum)
            self.curNum = node.val
            self.curNumCount = 1
        elif self.curNum==node.val:
            self.curNumCount += 1
        
        if node.right:
            self.inorder(node.right)
        
        if self.curNumCount > self.modeVal:
            self.modeVal = self.curNumCount
            self.modeArr = {self.curNum}
        elif self.curNumCount == self.modeVal:
            self.modeArr.add(self.curNum)
