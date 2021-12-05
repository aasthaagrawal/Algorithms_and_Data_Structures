#https://leetcode.com/problems/construct-string-from-binary-tree/
#Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.q = []
        self.constructPath(root)
        return "".join(self.q)
    
    def constructPath(self, node):
        self.q.append(str(node.val))
        if not node.left and not node.right:
            return
        if node.left:
            self.q.append('(')
            self.constructPath(node.left)
            self.q.append(')')
        if node.right:
            if not node.left:
                self.q.append('()')
            self.q.append('(')
            self.constructPath(node.right)
            self.q.append(')')
