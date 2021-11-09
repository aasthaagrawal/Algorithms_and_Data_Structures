#https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        self.distance = distance
        self.util(root)
        return self.result

    def util(self, node):
        if not node.left and not node.right:
            return {1: 1} #dist : num_leaf_node
        ldict,rdict = dict(), dict()
        if node.left:
            ldict = self.util(node.left)
        if node.right:
            rdict = self.util(node.right)
        for lk,lv in ldict.items():
            for rk,rv in rdict.items():
                if lk+rk <= self.distance:
                    self.result += (lv*rv)
        d = {}
        for lk,lv in ldict.items():
            if lk+1< self.distance:
                d[lk+1] = lv
        for rk,rv in rdict.items():
            if rk+1< self.distance:
                if rk+1 in d:
                    d[rk+1] += rv
                else:
                    d[rk+1] = rv
        return d
