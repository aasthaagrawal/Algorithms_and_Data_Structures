#https://leetcode.com/problems/binary-tree-paths/
#Time Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        self.util(root,"")
        return self.result

    def util(self, node, path):
        if path == "":
            path = str(node.val)
        else:
            path = path + "->" + str(node.val)
        if not node.left and not node.right:
            self.result.append(path[:])
            return
        if node.left:
            self.util(node.left, path)
        if node.right:
            self.util(node.right, path)
