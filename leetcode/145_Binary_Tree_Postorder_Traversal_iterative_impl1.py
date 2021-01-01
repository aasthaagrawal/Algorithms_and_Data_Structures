#https://leetcode.com/problems/binary-tree-postorder-traversal/
#Time Complexity: O(n)
#Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        ele = None
        while stack:
            if ele and stack and (ele is stack[-1].right or ele is stack[-1].left):
                ele = stack.pop()
                res.append(ele.val)
                continue
            ele = stack[-1]
            if ele.left or ele.right:
                if ele.right:
                    stack.append(ele.right)
                if ele.left:
                    stack.append(ele.left)
            else:
                res.append(ele.val)
                stack.pop()
        return res
