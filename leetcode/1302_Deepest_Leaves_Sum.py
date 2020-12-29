#https://leetcode.com/problems/deepest-leaves-sum/
#Time Complexity: O(n)
#Space Complexity: O(2^(d-1))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        curQ = [root]
        nextQ = []
        while curQ:
            for node in curQ:
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            if not nextQ:
                break
            curQ = nextQ
            nextQ = []
        res = 0
        for node in curQ:
            res += node.val
        return res
