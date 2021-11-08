#https://leetcode.com/problems/all-possible-full-binary-trees/
#Time Complexity: O(2^N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import copy
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.fbt = {0: [], 1: [TreeNode(0)]}
        self.util(n)
        return self.fbt[n]

    def util(self,n):
        if n in self.fbt:
            return self.fbt[n]
        self.fbt[n] = []
        if n%2 == 0:
            return self.fbt[n]
        root = TreeNode(0)
        for l in range(n):
            r = n-l-1
            print(l,r)
            for left in self.util(l):
                for right in self.util(r):
                    root.left = left
                    root.right = right
                    self.fbt[n].append(copy.deepcopy(root))
        return self.fbt[n]
