#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        self.nums = nums
        return self.util(0,len(nums)-1)

    def util(self, left, right):
        if left > right:
            return None
        elif left == right:
            return TreeNode(self.nums[left])
        elif right-left == 1:
            root = TreeNode(self.nums[right])
            root.left = TreeNode(self.nums[left])
            return root
        mid = left + (right - left)//2
        root = TreeNode(self.nums[mid])
        root.left = self.util(left, mid-1)
        root.right = self.util(mid+1, right)
        return root
