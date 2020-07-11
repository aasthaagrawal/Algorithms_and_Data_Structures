#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#Complexity: O(V+E)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result_stack = []
        curr_level = [root]
        next_level = []
        while len(curr_level) > 0:
            result_stack.append([])
            for node in curr_level:
                result_stack[-1].append(node.val)
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            curr_level = next_level
            next_level = []
        return result_stack[::-1]
