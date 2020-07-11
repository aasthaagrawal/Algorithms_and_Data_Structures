#https://leetcode.com/problems/average-of-levels-in-binary-tree/
#Complexity: O(V+E)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        curr_level = [root]
        next_level = []
        result = []
        while len(curr_level) > 0:
            sumC = 0
            lenC = 0
            for node in curr_level:
                sumC += node.val
                lenC += 1
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(sumC/lenC)
            curr_level = next_level
            next_level = []
        return result
