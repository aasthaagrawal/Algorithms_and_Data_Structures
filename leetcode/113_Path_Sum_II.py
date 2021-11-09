#https://leetcode.com/problems/path-sum-ii/
#Time Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.targetSum = targetSum
        self.result = []
        self.util(root,[],0)
        return self.result

    def util(self, node, path, pathSum):
        path.append(node.val)
        pathSum += node.val
        if not node.left and not node.right:
            if pathSum == self.targetSum:
                self.result.append(path[:])
        if node.left:
            self.util(node.left,path,pathSum)
        if node.right:
            self.util(node.right,path,pathSum)
        path.pop()
        pathSum -= node.val
