#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
#Time complexity: O(N log N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []
        q = [(0,0,root)]
        level= 0
        while q:
            col, level, node = q.pop(0)
            node_list.append((col, level, node.val))
            if node.left:
                q.append((col-1, level+1, node.left))
            if node.right:
                q.append((col+1, level+1, node.right))
        node_list.sort()
        result = [[]]
        cur_col = node_list[0][0]
        for col,level,val in node_list:
            if col != cur_col:
                result.append([])
                cur_col = col
            result[-1].append(val)
        return result
