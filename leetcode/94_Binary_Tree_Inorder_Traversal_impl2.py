#https://leetcode.com/problems/binary-tree-inorder-traversal/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if len(stack)<=0:
                break
            root=stack.pop(-1)
            result.append(root.val)
            root=root.right
        return result
