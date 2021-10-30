#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#Time Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cur_st = [root]
        next_st = []
        left_to_right = True
        result = []
        while cur_st:
            result.append([])
            while cur_st:
                node = cur_st.pop()
                result[-1].append(node.val)
                if left_to_right:
                    if node.left:
                        next_st.append(node.left)
                    if node.right:
                        next_st.append(node.right)
                else:
                    if node.right:
                        next_st.append(node.right)
                    if node.left:
                        next_st.append(node.left)
            left_to_right = not left_to_right
            cur_st = next_st
            next_st = []
        return result
