#https://leetcode.com/problems/sum-of-left-leaves/
#Complexity: O(n)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum=0   
        def leftLeavesSum(root):
            if not root:
                return 0
            if root.left and not root.left.left and not root.left.right:
                self.sum+=root.left.val
            leftLeavesSum(root.left)
            leftLeavesSum(root.right)
        
        leftLeavesSum(root)
        return self.sum
