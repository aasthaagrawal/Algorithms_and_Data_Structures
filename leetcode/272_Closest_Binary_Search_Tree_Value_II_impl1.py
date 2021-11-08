#https://leetcode.com/problems/closest-binary-search-tree-value-ii/
#Space Complexity: O(k)
#Time Complexity: O(NlogK)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import heapq
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.closest = []
        heapq.heapify(self.closest)
        self.target = target
        self.k = k
        self.inorder(root)
        return [x2 for x1,x2 in self.closest]

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        heapq.heappush(self.closest,(-1*abs(self.target-node.val),node.val))
        if len(self.closest)>self.k:
            heapq.heappop(self.closest)
        self.inorder(node.right)
