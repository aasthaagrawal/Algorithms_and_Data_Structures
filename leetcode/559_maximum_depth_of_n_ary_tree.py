#https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        maxDepth = 0
        nextLevel = []
        curLevel = [root]
        while len(curLevel) != 0:
            maxDepth += 1
            for node in curLevel:
                if node.children != None:
                    nextLevel.extend(node.children)
            curLevel = nextLevel
            nextLevel = []
        return maxDepth
