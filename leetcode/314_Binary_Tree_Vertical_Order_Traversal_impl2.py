#https://leetcode.com/problems/binary-tree-vertical-order-traversal/
#Time Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_dict = defaultdict(list)
        q = [(root,0)]
        min_col = float("inf")
        max_col = -float("inf")
        while q:
            node, col = q.pop(0)
            column_dict[col].append(node.val)
            if col<min_col:
                min_col = col
            if col>max_col:
                max_col = col

            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        result = []
        for i in range(min_col,max_col+1):
            if column_dict[i]:
                result.append(column_dict[i])
        return result
